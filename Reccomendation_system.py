#RECOMMENDATION SYSTEM
#Developed by Pavithra Praveen as part of CodSoft AI Internship

#Import the required libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Sample movie data (title and genre)
movies = {
    'title': ['Inception', 'Interstellar', 'The Dark Knight', 'Titanic', 'Avengers', 'The Notebook'],
    'genre': ['Sci-Fi', 'Sci-Fi', 'Action', 'Romance', 'Action', 'Romance']
}

#Create a DataFrame from the dictionary
df=pd.DataFrame(movies)

#We’ll use the genre column as the feature to compare movies
df['features']=df['genre']

#Convert the text features into numerical data
vectorizer=CountVectorizer()
feature_matrix=vectorizer.fit_transform(df['features'])

#Use cosine similarity to compare how close the movies are
similarity=cosine_similarity(feature_matrix)

#Function to get movie recommendations
def recommend(title):
    if title not in df['title'].values:
        return "Sorry, this movie is not in the list."
    
    movie_index=df[df['title'] == title].index[0]
    scores=list(enumerate(similarity[movie_index]))
    scores=sorted(scores, key=lambda x: x[1], reverse=True)
    
    #Skip the first one (it will be the same movie)
    recommended=[]
    for i in scores[1:4]:
        recommended.append(df['title'][i[0]])
    
    return recommended

#Ask user for input
user_input=input("Enter a movie name: ")
result=recommend(user_input)

#Show the results
if isinstance(result,list):
    print("Recommended movies:")
    for movie in result:
        print("-",movie)
else:
    print(result)
