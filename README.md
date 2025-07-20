# Movie-Review-Data-Analysis

**Movie-Review-Data-Analysis** is an ETL pipeline built in Python to process the classic MovieLens dataset, integrating movie ratings, user demographics, and movie metadata into a clean, unified format. The processed data is loaded into an SQLite database and basic visual analytics on genres and user demographics are provided.. This project was done as a part of The Fundamentals of Data Engineering course at RV University.
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
  Mapping of genre indices to names (e.g. 1: Action, 5: Comedy, 19: Western)  (Not Used)

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

2. **Run the Pipeline**

`python main.py`

This will:

- Read and clean the MovieLens files (`u.data`, `u.user`, `u.item`)  
- Merge into a comprehensive dataset  
- Store results in a local SQLite database  
- Display database summary and samples  
- Generate and show visualizations on genres and user demographics

---

## Visualizations Provided

- **Genre Distribution**: Number of movies per major genre (e.g., Action, Comedy, Drama)  
- **Age Distribution**: Histogram of user ages  
- **Gender Distribution**: Counts of Male vs Female users  
- **Top Occupations**: Bar chart listing the 10 most common user occupations  

---

## Notes

- Only genre flags 1-19 are retained; 20-23 are discarded due to insufficient data.  
- The project focuses on data engineering and exploratory analysis; it forms a base for further machine learning or recommendation systems.  
- SQLite DB file `movies_database.db` can be queried externally for ad hoc analysis.  

---


_For detailed code execution flow and data handling, review the source scripts: `extract.py`, `transform.py`, `load.py`, and `main.py`._

   
