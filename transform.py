import pandas as pd

def clean_data(u_data, u_user, u_item):
    # Clean the dataframes by dropping rows with missing values
    u_data_cleaned = u_data.dropna()
    u_user_cleaned = u_user.dropna()
    u_item_cleaned = u_item.drop(columns=['video_release_date',"genre_20", "genre_21", 'genre_22' , 'genre_23'])

    # Merge u_data with u_item on movie_id
    merged_data = pd.merge(u_data_cleaned, u_item_cleaned, on="movie_id")
    merged_data = merged_data.dropna()
    # Merge the result with u_user on user_id
    final_merged_data = pd.merge(merged_data, u_user_cleaned, on="user_id")

    return final_merged_data
