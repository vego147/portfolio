import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)


movies = pd.read_csv('pygame\ML\movies.csv')

movies['genres'] =movies['genres'].fillna("").str.replace("|", " ").str.lower() 

print(movies.head())

tfidf = TfidfVectorizer(stop_words = 'english')

tfidf_matrix = tfidf.fit_transform(movies['genres'])

cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

print(cos_sim.shape)

def recommndation(title , cos_sim):
    idx = movies.index[movies['title']== title].tolist()
    if not idx:
        return "Movie Not Found"
    idx = idx[0]
    sim_scores = list(enumerate(cos_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse =True)
    top_movies = sim_scores[1:11]
    recommended_movies = [movies.iloc[i[0]]['title'] for i in top_movies]
    return recommended_movies





while True:
    user = input("enter the movie Name You want recommendations: ")

    if user == "quit":
        break
    else:   
        print(recommndation(user, cos_sim))

   