import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def load_to_sqlite(final_merged_data, db_name='movies_database.db'):
    """
    Function to load the final merged data into an SQLite database.

    Parameters:
    final_merged_data (pd.DataFrame): The final merged DataFrame to be loaded into the database.
    db_name (str): The name of the SQLite database file. Defaults to 'movies_database.db'.
    """
    # Create a connection to the SQLite database (it will create the database file if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the table schema (same as before)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movie_ratings (
        user_id INTEGER,
        movie_id INTEGER,
        rating INTEGER,
        timestamp INTEGER,
        title TEXT,
        release_date TEXT,
        IMDb_URL TEXT,
        genre_1 INTEGER,
        genre_2 INTEGER,
        genre_3 INTEGER,
        genre_4 INTEGER,
        genre_5 INTEGER,
        genre_6 INTEGER,
        genre_7 INTEGER,
        genre_8 INTEGER,
        genre_9 INTEGER,
        genre_10 INTEGER,
        genre_11 INTEGER,
        genre_12 INTEGER,
        genre_13 INTEGER,
        genre_14 INTEGER,
        genre_15 INTEGER,
        genre_16 INTEGER,
        genre_17 INTEGER,
        genre_18 INTEGER,
        genre_19 INTEGER,
        age INTEGER,
        gender TEXT,
        occupation TEXT,
        zip_code TEXT
    )
    """)

    # Load data into the database
    final_merged_data.to_sql('movie_ratings', conn, if_exists='replace', index=False)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print(f"Data has been successfully loaded into the SQLite database: {db_name}")

def plot_genre_distribution(final_merged_data):
    # Create a new column that lists the genres for each movie
    genre_columns = [f'genre_{i}' for i in range(1, 24)]
    genre_names = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", 
                   "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]
    
    # Assign genre names
    for i, genre_name in enumerate(genre_names):
        final_merged_data[genre_name] = final_merged_data[genre_columns[i]]

    # Group by genre and count the number of movies for each genre
    genre_count = final_merged_data[genre_names].sum()

    # Plot the genre distribution
    plt.figure(figsize=(10, 6))
    genre_count.sort_values(ascending=False).plot(kind='bar')
    plt.title('Genre Distribution in the Movie Dataset')
    plt.ylabel('Number of Movies')
    plt.xlabel('Genres')
    plt.xticks(rotation=45)
    plt.show()

def user_demographics_analysis(final_merged_data):
    # User demographics analysis: Age, Gender, Occupation
    plt.figure(figsize=(10, 6))
    final_merged_data['age'].hist(bins=20)
    plt.title('Age Distribution of Users')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

    gender_count = final_merged_data['gender'].value_counts()
    gender_count.plot(kind='bar', title='Gender Distribution of Users')
    plt.xlabel('Gender')
    plt.ylabel('Frequency')
    plt.show()

    occupation_count = final_merged_data['occupation'].value_counts().head(10)  # Top 10 occupations
    occupation_count.plot(kind='bar', title='Top 10 Occupations of Users')
    plt.xlabel('Occupation')
    plt.ylabel('Frequency')
    plt.show()

# Genre names (this is defined here so it's accessible in every plot function)
genre_names = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", 
               "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]

# 1. Plot: Average Genre Ratings by Age Group
def plot_genre_ratings_by_age_group(final_merged_data):
    # Create a "genres" column with the genre names
    genre_columns = [f'genre_{i}' for i in range(1, 24)]
    
    for i, genre_name in enumerate(genre_names):
        final_merged_data[genre_name] = final_merged_data[genre_columns[i]]

    # Create age groups
    bins = [0, 18, 30, 40, 50, 60, 100]
    labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '60+']
    final_merged_data['age_group'] = pd.cut(final_merged_data['age'], bins=bins, labels=labels, right=False)

    # Group by age group and genre, then calculate the average rating
    genre_age_rating = final_merged_data.groupby(['age_group'])[genre_names].mean()
    
    # Plot the genre ratings by age group
    genre_age_rating.plot(kind='bar', figsize=(12, 6), width=0.8)
    plt.title('Average Genre Ratings by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()  # This fixes the margin issue
    plt.show()  # Only one call to plt.show() here


# 2. Plot: Average Genre Ratings by Gender
def plot_genre_ratings_by_gender(final_merged_data):
    # Create a "genres" column with the genre names
    genre_columns = [f'genre_{i}' for i in range(1, 24)]
    
    for i, genre_name in enumerate(genre_names):
        final_merged_data[genre_name] = final_merged_data[genre_columns[i]]

    # Group by gender and genre, then calculate the average rating
    genre_gender_rating = final_merged_data.groupby(['gender'])[genre_names].mean()

    # Plot the genre ratings by gender
    genre_gender_rating.plot(kind='bar', figsize=(12, 6), width=0.8)
    plt.title('Average Genre Ratings by Gender')
    plt.xlabel('Genres')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Gender', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()  # This fixes the margin issue
    plt.show()  # Only one call to plt.show() here


# 3. Plot: Average Genre Ratings by Top 5 Occupations
def plot_genre_ratings_by_top_occupations(final_merged_data):
    # Get the top 5 occupations
    top_occupations = final_merged_data['occupation'].value_counts().head(5).index
    # Filter the data for top occupations
    filtered_data = final_merged_data[final_merged_data['occupation'].isin(top_occupations)].copy()  # Explicitly make a copy

    # Create a "genres" column with the genre names
    genre_columns = [f'genre_{i}' for i in range(1, 24)]
    
    # Assign genre names to the filtered data using .loc to avoid the warning
    for i, genre_name in enumerate(genre_names):
        filtered_data.loc[:, genre_name] = filtered_data[genre_columns[i]]  # Use .loc[] to modify safely

    # Group by occupation and genre, then calculate the average rating
    genre_occupation_rating = filtered_data.groupby(['occupation'])[genre_names].mean()

    # Plot the genre ratings by top 5 occupations
    genre_occupation_rating.plot(kind='bar', figsize=(12, 6), width=0.8)
    plt.title('Average Genre Ratings by Top 5 Occupations')
    plt.xlabel('Genres')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Occupation', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()  # This fixes the margin issue
    plt.show()  # Only one call to plt.show() here