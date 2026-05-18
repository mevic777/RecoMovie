import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def prepare_data_soup(all_movies, genre_map_id_to_name):
    df = pd.DataFrame(all_movies)

    def get_genre_names(genre_ids):
        return " ".join([genre_map_id_to_name.get(gid, "") for gid in genre_ids])

    df["genre_names"] = df["genre_ids"].apply(get_genre_names)
    df["overview"] = df["overview"].fillna("")

    df["soup"] = df["genre_names"] + " " + df["genre_names"] + " " + df["overview"]

    return df


def get_hybrid_recommendations(selected_movies_ids, all_movies, genre_map):
    df = prepare_data_soup(all_movies, genre_map)

    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["soup"])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(df.index, index=df["id"]).drop_duplicates()

    sim_scores_total = None

    for m_id in selected_movies_ids:
        if m_id not in indices:
            continue

        idx = indices[m_id]
        sim_scores = cosine_sim[idx]

        if sim_scores_total is None:
            sim_scores_total = sim_scores
        else:
            sim_scores_total += sim_scores

    if sim_scores_total is None:
        return []

    movie_indices = sim_scores_total.argsort()[::-1]

    final_indices = [
        i for i in movie_indices if df.iloc[i]["id"] not in selected_movies_ids
    ]

    return df.iloc[final_indices[:21]].to_dict("records")
