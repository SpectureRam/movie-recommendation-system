import os
import gdown
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
import streamlit as st

# Google Drive file IDs
movies_file_id = "1HWlVK-nXM5JG4GfSDHyR-x8T1AlfQQYw"
ratings_file_id = "1V2s1rpu4Gfjbt8z2a1Xml9IJr5KSozK1"


# Download the files if they don't exist
def download_file_from_google_drive(file_id, output):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output, quiet=False)


if not os.path.exists("movies.csv"):
    download_file_from_google_drive(movies_file_id, "movies.csv")

if not os.path.exists("ratings.csv"):
    download_file_from_google_drive(ratings_file_id, "ratings.csv")

# Load the data
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")


# Clean movie titles
def clean_title(title):
    title = re.sub("[^a-zA-Z0-9 ]", "", title)
    return title


movies["clean_title"] = movies["title"].apply(clean_title)

# Vectorize the titles
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf = vectorizer.fit_transform(movies["clean_title"])


# Function to search for movies
def search(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indices].iloc[::-1]
    return results


# Function to find similar movies
def find_similar_movies(movie_id):
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

    similar_user_recs = similar_user_recs[similar_user_recs > .10]
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]

    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]


# Streamlit UI
st.title("Movie Recommendation System")

movie_name = st.text_input("Enter a movie title", "Toy Story")

if len(movie_name) > 5:
    results = search(movie_name)
    if not results.empty:
        movie_id = results.iloc[0]["movieId"]
        st.write(f"Top recommendations based on '{results.iloc[0]['title']}':")
        recommendations = find_similar_movies(movie_id)
        for index, row in recommendations.iterrows():
            st.write(f"{row['title']} ({row['genres']}) - Score: {row['score']:.2f}")
    else:
        st.write("No movies found. Please try a different title.")