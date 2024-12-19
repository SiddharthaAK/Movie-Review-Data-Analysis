import pandas as pd

def load_data():
    # Load datasets
    u_data = pd.read_csv("u.data", sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])
    u_user = pd.read_csv("u.user", sep="|", names=["user_id", "age", "gender", "occupation", "zip_code"])
    u_item = pd.read_csv("u.item", sep="|", names=["movie_id", "title", "release_date", "video_release_date", "IMDb_URL"] + [f"genre_{i}" for i in range(1, 24)], encoding='ISO-8859-1')

    return u_data, u_user, u_item
