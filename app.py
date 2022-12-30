import streamlit as st
import pickle
import requests

similarity = pickle.load(open('similarity1.pkl', 'rb'))
movies = pickle.load(open('movies1.pkl', 'rb'))
movies_list = movies['title']

"""
fetch_poster fucntion helps to fectch movie poster using movie id. 
it takes one argument movie_id
"""
def fetch_poster(movie_id):
    api = "https://api.themoviedb.org/3/movie/{}?api_key=e54fb75f9c426527afcf89a6ee0da61b".format(movie_id)
    print(api)
    data = requests.get(api)
    data = data.json()
    # print(data)
    poster_path = data['poster_path']
    # print(poster_path)
    if poster_path == None:
        poster_path = ""
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
"""
Recommend_movies function recommend the movies.
it takes one argument movie_name.
"""
def Recommend_movies(movie_name):
    movie = movie_name.lower()
    if movie not in movies['title'].unique():
        print(f"Sorry! The movie {movie} you requested is not found in our database. Please check the spelling or try with some other movies")
    else:
        index_val = movies[movies['title'] == movie].index[0]
        similar_movies = sorted(list(enumerate(similarity[index_val])),reverse=True, key=lambda x:x[1])

        recommeded_movies = []
        recommended_movies_posters = []
        for i in similar_movies[0:11]:
            movie_id = movies.iloc[i[0]].id
            recommended_movies_posters.append(fetch_poster(movie_id))
            recommeded_movies.append(movies.iloc[i[0]].title)
            
        return recommeded_movies, recommended_movies_posters

bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://cdn.mos.cms.futurecdn.net/Ps8mZvho7kJHiWnUhyUqug.png");
background-size: cover;
}
[data-testid="stHeader"]{
    background-color : rgba(0,0,0,0);
}
</style>
"""
st.markdown(bg_img, unsafe_allow_html=True)
st.title('Movies Recommendation System')

select_movie = st.selectbox(
    'Discover movies by the one Click',
    movies_list)

if st.button('Recommend'):
    recommeded_movies, recommended_movies_posters = Recommend_movies(select_movie)
    # for i in recommendation:
    #     st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)

    with col1:
        st.text(recommeded_movies[0])
        st.image(recommended_movies_posters[0])

    with col2:
        st.text(recommeded_movies[1])
        st.image(recommended_movies_posters[1])

    with col3:
        st.text(recommeded_movies[2])
        st.image(recommended_movies_posters[2])

    with col4:
        st.text(recommeded_movies[3])
        st.image(recommended_movies_posters[3])

    with col5:
        st.text(recommeded_movies[4])
        st.image(recommended_movies_posters[4])

    with col6:
        st.text(recommeded_movies[5])
        st.image(recommended_movies_posters[5])

    with col7:
        st.text(recommeded_movies[6])
        st.image(recommended_movies_posters[6])

    with col8:
        st.text(recommeded_movies[7])
        st.image(recommended_movies_posters[7])

    with col9:
        st.text(recommeded_movies[8])
        st.image(recommended_movies_posters[8])

    with col10:
        st.text(recommeded_movies[9])
        st.image(recommended_movies_posters[9])

    