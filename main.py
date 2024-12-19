import sqlite3

from extract import load_data
from transform import clean_data
from load import load_to_sqlite, plot_genre_distribution, user_demographics_analysis,plot_genre_ratings_by_age_group, plot_genre_ratings_by_gender, plot_genre_ratings_by_top_occupations

def main():
    # Step 1: Extract
    u_data, u_user, u_item = load_data()

    # Step 2: Transform
    final_merged_data = clean_data(u_data, u_user, u_item)

    # Step 3: Load - Insert into SQLite Database
    load_to_sqlite(final_merged_data, db_name='movies_database.db')

    # Step 4: Open the SQLite Database to confirm data is loaded
    print("Opening the SQLite Database and running a query...\n")
    conn = sqlite3.connect('movies_database.db')  # Connect to the SQLite database
    cursor = conn.cursor()

    # Example query to check if data is loaded
    cursor.execute("SELECT COUNT(*) FROM movie_ratings;")  # Counting the number of rows in the table
    result = cursor.fetchone()
    print(f"Number of rows in 'movie_ratings' table: {result[0]}\n")

    # Example query to view some data from the table (optional)
    cursor.execute("SELECT * FROM movie_ratings LIMIT 5;")  # Retrieve the first 5 rows from the table
    rows = cursor.fetchall()
    print("First 5 rows in the 'movie_ratings' table:")
    for row in rows:
        print(row)

    # Close the connection to the database
    conn.close()

    # Step 5: Reporting - Data Analysis and Visualization
    print("\nStarting genre distribution plotting...")
    plot_genre_distribution(final_merged_data)
    print("\nStarting user demographics analysis...")
    user_demographics_analysis(final_merged_data)
    # Run the visualizations after the data is processed
    plot_genre_ratings_by_age_group(final_merged_data)
    plot_genre_ratings_by_gender(final_merged_data)
    plot_genre_ratings_by_top_occupations(final_merged_data)

if __name__ == "__main__":
    main()
