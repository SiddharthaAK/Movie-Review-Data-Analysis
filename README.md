# Movie-Review-Data-Analysis
Created an ETL pipeline to handle a dataset of movie reviews. This project was done as a part of The Fundamentals of Data Engineering course at RV University.
Currently working on building a recommendation system using this data, will be deployed on 1st August.

---

## Dataset Files and Their Contents

- **u.data**  
  Contains movie rating records with the following columns:  
  - `user_id`: ID of the user giving the rating  
  - `movie_id`: ID of the movie being rated  
  - `rating`: Integer rating (e.g., 1-5)  
  - `timestamp`: Time the rating was recorded  

- **u.user**  
  User demographic information, including:  
  - `user_id`  
  - `age`  
  - `gender` (M/F)  
  - `occupation`  
  - `zip_code`  

- **u.item**  
  Movie metadata with columns:  
  - `movie_id`  
  - `title`  
  - `release_date`  
  - `video_release_date` (dropped during cleaning, contains mostly nulls)  
  - `IMDb_URL`  
  - `genre_1` to `genre_23`: Binary flags indicating movie genres (only genres 1 to 19 retained, 20-23 dropped)  

- **u.genre**  
  Mapping of genre indices to names (e.g. 1: Action, 5: Comedy, 19: Western)  

---

## ETL Pipeline Components

### 1. Extract (`extract.py`)

- Loads the three datasets using pandas with appropriate separators and column names.  
- `u.item` is loaded with `ISO-8859-1` encoding to handle special characters.

### 2. Transform (`transform.py`)

- Cleans data by dropping rows with missing values (`NaN`).  
- Drops `video_release_date` and genres 20-23 from `u.item` due to null values.  
- Merges the datasets sequentially:  
  - Ratings (`u.data`) joined with movie metadata (`u.item`) on `movie_id`  
  - Result then joined with user data (`u.user`) on `user_id`  
- Produces a single merged DataFrame containing ratings, full movie info, and user demographics.

### 3. Load (`load.py`)

- Saves the final merged DataFrame to an SQLite database named `movies_database.db` into a table called `movie_ratings`.  
- Table schema includes all merged columns: user info, movie info, ratings, and genres.  
- Provides visualization functions:  
  - **Genre distribution**: Bar chart showing number of movies per genre  
  - **User demographics**:  
    - Age distribution histogram  
    - Gender distribution bar chart  
    - Top 10 user occupations bar chart

### 4. Execute Pipeline (`main.py`)

- Runs ETL steps in sequence: extract, transform, load.  
- Displays sample merged data.  
- Executes example SQL queries on SQLite DB to confirm data load (e.g., count of records, first 5 rows).  
- Triggers plotting functions to visualize key insights.

---

## How to Use

1. **Install Dependencies**

`pip install pandas matplotlib sqlite3`

   
