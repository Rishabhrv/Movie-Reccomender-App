import streamlit as st
import pickle
import requests
from PIL import Image

# Load movie data, similarity data, top 20 movies and top grossing movies
movies = pickle.load(open('movie_list.pkl', 'rb')) 
movies_list = movies['title'].values # Extract movie titles from movie data
similarity = pickle.load(open('similarity.pkl', 'rb')) # Load similarity data
top20 = pickle.load(open('top20.pkl', 'rb')) # Load top 20 movies data
top_grossing = pickle.load(open('top_grossing.pkl', 'rb')) # Load top grossing movies data

image = Image.open('myimage.jpg') # Open the image file that will be displayed later in the app

# Function to recommend movies based on the similarity of movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0] # Get the index of the movie
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]) # Sort the similarity scores in descending order
    recommended_movies = [] # Initialize an empty list for recommended movies
    recommended_movie_posters = [] # Initialize an empty list for recommended movie posters
    for i in distances[1:6]: # Loop through the top 5 similar movies (excluding the input movie)
        movie_id = movies.iloc[i[0]].movie_id # Get the movie ID
        recommended_movie_posters.append(fetch_poster(movie_id)) # Fetch the movie poster and add it to the list of recommended movie posters
        recommended_movies.append(movies.iloc[i[0]].title) # Add the movie title to the list of recommended movies
    return recommended_movies, recommended_movie_posters # Return the recommended movies and their posters

# Function to fetch the poster of a movie using an API provided by The Movie Database (TMDb)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id) # Construct the URL for fetching the movie data
    data = requests.get(url) # Make an HTTP request to fetch the movie data
    data = data.json() # Convert the response to a JSON object
    poster_path = data['poster_path'] # Extract the poster path from the JSON object
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path # Construct the URL for the poster image
    return full_path # Return the URL for the poster image

# Function to return the title of a movie along with its release year
def title(df, index):
    tit = df['title'].values[index] # Extract the movie title
    num = df['year'][index].astype(int) # Extract the release year as an integer
    num = num.astype(str) # Convert the release year to a string
    return tit + ' ' + "(" + num + ")" # Return the title of the movie along with its release year

# Function to return the rating of a movie from the top 20 movies
def caption(index):
    return 'Ratings : ' + top20['vote_average'].values[index].astype(str) # Extract the rating of the movie from the top 20 movies and return it as a string


#This function takes an index as input and returns the revenue information of the movie located at that index
def revenew(index):
    return 'Revenue : ' + '$' + top_grossing['revenue'].values[index].astype(str) + 'M'


st.title('Movie Recommender')

st.sidebar.write('Built By -')
st.sidebar.title('Rishabh Vyas')
st.sidebar.image(image, caption='Machine Learning Engineer', width=160)
st.sidebar.write('E-mail - rishabhvyas472@gmail.com')

tab1, tab2, tab3 = st.tabs(['Movie Recommender', 'Top Movies', 'Top Grossing'])

# -------------------------------Tab 1----------------------------------------#

with tab1:
    st.header('Movie Recommender')

selected_movie = st.selectbox('Type Movie name to search or you can select also!', movies_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.write(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.write(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.write(recommended_movie_names[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.write(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.write(recommended_movie_names[4])

# ------------------------------------Tab 2-------------------------------------------#

with tab2:
    st.header('Top 30 Movies')

    col1, col2, col3, col4, col5 = st.columns(5, gap="small")

    with col1:
        st.image(fetch_poster(top20['movie_id'].values[0]))
        st.write(title(top20, 0))
        st.caption(caption(0))

    with col2:
        st.image(fetch_poster(top20['movie_id'].values[1]))
        st.write(title(top20, 1))
        st.caption(caption(1))

    with col3:
        st.image(fetch_poster(top20['movie_id'].values[2]))
        st.write(title(top20, 2))
        st.caption(caption(2))

    with col4:
        st.image(fetch_poster(top20['movie_id'].values[3]))
        st.write(title(top20, 3))
        st.caption(caption(3))

    with col5:
        st.image(fetch_poster(top20['movie_id'].values[4]))
        st.write(title(top20, 4))
        st.caption(caption(4))

        # -----------second row---------------#

    col6, col7, col8, col9, col10 = st.columns(5, gap="small")

    with col6:
        st.image(fetch_poster(top20['movie_id'].values[5]))
        st.write(title(top20, 5))
        st.caption(caption(5))

    with col7:
        st.image(fetch_poster(top20['movie_id'].values[6]))
        st.write(title(top20, 6))
        st.caption(caption(6))

    with col8:
        st.image(fetch_poster(top20['movie_id'].values[7]))
        st.write(title(top20, 7))
        st.caption(caption(7))

    with col9:
        st.image(fetch_poster(top20['movie_id'].values[8]))
        st.write(title(top20, 8))
        st.caption(caption(8))

    with col10:
        st.image(fetch_poster(top20['movie_id'].values[9]))
        st.write(title(top20, 9))
        st.caption(caption(9))

        # ---------Third row---------------

    col11, col12, col13, col14, col15 = st.columns(5, gap="small")

    with col11:
        st.image(fetch_poster(top20['movie_id'].values[10]))
        st.write(title(top20, 10))
        st.caption(caption(10))

    with col12:
        st.image(fetch_poster(top20['movie_id'].values[11]))
        st.write(title(top20, 11))
        st.caption(caption(11))

    with col13:
        st.image(fetch_poster(top20['movie_id'].values[12]))
        st.write(title(top20, 12))
        st.caption(caption(12))

    with col14:
        st.image(fetch_poster(top20['movie_id'].values[13]))
        st.write(title(top20, 13))
        st.caption(caption(13))

    with col15:
        st.image(fetch_poster(top20['movie_id'].values[14]))
        st.write(title(top20, 14))
        st.caption(caption(14))

        # ------------ Fourth Row-------------#

    col16, col17, col18, col19, col20 = st.columns(5, gap="small")

    with col16:
        st.image(fetch_poster(top20['movie_id'].values[15]))
        st.write(title(top20, 15))
        st.caption(caption(15))

    with col17:
        st.image(fetch_poster(top20['movie_id'].values[16]))
        st.write(title(top20, 16))
        st.caption(caption(16))

    with col18:
        st.image(fetch_poster(top20['movie_id'].values[17]))
        st.write(title(top20, 17))
        st.caption(caption(17))

    with col19:
        st.image(fetch_poster(top20['movie_id'].values[18]))
        st.write(title(top20, 18))
        st.caption(caption(18))

    with col20:
        st.image(fetch_poster(top20['movie_id'].values[19]))
        st.write(title(top20, 19))
        st.caption(caption(19))

        # ------------ Fifth Row-------------#

    col21, col22, col23, col24, col25 = st.columns(5, gap="small")

    with col21:
        st.image(fetch_poster(top20['movie_id'].values[20]))
        st.write(title(top20, 20))
        st.caption(caption(20))

    with col22:
        st.image(fetch_poster(top20['movie_id'].values[21]))
        st.write(title(top20, 21))
        st.caption(caption(21))

    with col23:
        st.image(fetch_poster(top20['movie_id'].values[22]))
        st.write(title(top20, 22))
        st.caption(caption(22))

    with col24:
        st.image(fetch_poster(top20['movie_id'].values[23]))
        st.write(title(top20, 23))
        st.caption(caption(23))

    with col25:
        st.image(fetch_poster(top20['movie_id'].values[24]))
        st.write(title(top20, 24))
        st.caption(caption(24))

        # ------------ Sixth Row-------------#

    col26, col27, col28, col29, col30 = st.columns(5, gap="small")

    with col26:
        st.image(fetch_poster(top20['movie_id'].values[25]))
        st.write(title(top20, 25))
        st.caption(caption(25))

    with col27:
        st.image(fetch_poster(top20['movie_id'].values[26]))
        st.write(title(top20, 26))
        st.caption(caption(26))

    with col28:
        st.image(fetch_poster(top20['movie_id'].values[27]))
        st.write(title(top20, 27))
        st.caption(caption(27))

    with col29:
        st.image(fetch_poster(top20['movie_id'].values[28]))
        st.write(title(top20, 28))
        st.caption(caption(28))

    with col30:
        st.image(fetch_poster(top20['movie_id'].values[29]))
        st.write(title(top20, 29))
        st.caption(caption(29))

# ------------------------------Tab 3 ----------------------------------------#


with tab3:
    st.header('Top Grossing Movies of All Time')

    col1, col2, col3, col4, col5 = st.columns(5, gap="small")

    with col1:
        st.image(fetch_poster(top_grossing['movie_id'].values[0]))
        st.write(title(top_grossing, 0))
        st.caption(revenew(0))

    with col2:
        st.image(fetch_poster(top_grossing['movie_id'].values[1]))
        st.write(title(top_grossing, 1))
        st.caption(revenew(1))

    with col3:
        st.image(fetch_poster(top_grossing['movie_id'].values[2]))
        st.write(title(top_grossing, 2))
        st.caption(revenew(2))

    with col4:
        st.image(fetch_poster(top_grossing['movie_id'].values[3]))
        st.write(title(top_grossing, 3))
        st.caption(revenew(3))

    with col5:
        st.image(fetch_poster(top_grossing['movie_id'].values[4]))
        st.write(title(top_grossing, 4))
        st.caption(revenew(4))

        # -----------second row---------------#

    col6, col7, col8, col9, col10 = st.columns(5, gap="small")

    with col6:
        st.image(fetch_poster(top_grossing['movie_id'].values[5]))
        st.write(title(top_grossing, 5))
        st.caption(revenew(5))

    with col7:
        st.image(fetch_poster(top_grossing['movie_id'].values[6]))
        st.write(title(top_grossing, 6))
        st.caption(revenew(6))

    with col8:
        st.image(fetch_poster(top_grossing['movie_id'].values[7]))
        st.write(title(top_grossing, 7))
        st.caption(revenew(7))

    with col9:
        st.image(fetch_poster(top_grossing['movie_id'].values[8]))
        st.write(title(top_grossing, 8))
        st.caption(revenew(8))

    with col10:
        st.image(fetch_poster(top_grossing['movie_id'].values[9]))
        st.write(title(top_grossing, 9))
        st.caption(revenew(9))

        # ---------Third row---------------

    col11, col12, col13, col14, col15 = st.columns(5, gap="small")

    with col11:
        st.image(fetch_poster(top_grossing['movie_id'].values[10]))
        st.write(title(top_grossing, 10))
        st.caption(revenew(10))

    with col12:
        st.image(fetch_poster(top_grossing['movie_id'].values[11]))
        st.write(title(top_grossing, 11))
        st.caption(revenew(11))

    with col13:
        st.image(fetch_poster(top_grossing['movie_id'].values[12]))
        st.write(title(top_grossing, 12))
        st.caption(revenew(12))

    with col14:
        st.image(fetch_poster(top_grossing['movie_id'].values[13]))
        st.write(title(top_grossing, 13))
        st.caption(revenew(13))

    with col15:
        st.image(fetch_poster(top_grossing['movie_id'].values[14]))
        st.write(title(top_grossing, 14))
        st.caption(revenew(14))

        # ------------ Fourth Row-------------#

    col16, col17, col18, col19, col20 = st.columns(5, gap="small")

    with col16:
        st.image(fetch_poster(top_grossing['movie_id'].values[15]))
        st.write(title(top_grossing, 15))
        st.caption(revenew(15))

    with col17:
        st.image(fetch_poster(top_grossing['movie_id'].values[16]))
        st.write(title(top_grossing, 16))
        st.caption(revenew(16))

    with col18:
        st.image(fetch_poster(top_grossing['movie_id'].values[17]))
        st.write(title(top_grossing, 17))
        st.caption(revenew(17))

    with col19:
        st.image(fetch_poster(top_grossing['movie_id'].values[18]))
        st.write(title(top_grossing, 18))
        st.caption(revenew(18))

    with col20:
        st.image(fetch_poster(top_grossing['movie_id'].values[19]))
        st.write(title(top_grossing, 19))
        st.caption(revenew(19))

    # ------------ Fourth Row-------------#

    col21, col22, col23, col24, col25 = st.columns(5, gap="small")

    with col21:
        st.image(fetch_poster(top_grossing['movie_id'].values[20]))
        st.write(title(top_grossing, 20))
        st.caption(revenew(20))

    with col22:
        st.image(fetch_poster(top_grossing['movie_id'].values[21]))
        st.write(title(top_grossing, 21))
        st.caption(revenew(21))

    with col23:
        st.image(fetch_poster(top_grossing['movie_id'].values[22]))
        st.write(title(top_grossing, 22))
        st.caption(revenew(22))

    with col24:
        st.image(fetch_poster(top_grossing['movie_id'].values[23]))
        st.write(title(top_grossing, 23))
        st.caption(revenew(23))

    with col25:
        st.image(fetch_poster(top_grossing['movie_id'].values[24]))
        st.write(title(top_grossing, 24))
        st.caption(revenew(24))

    # ------------ Sixth Row-------------#

    col26, col27, col28, col29, col30 = st.columns(5, gap="small")

    with col26:
        st.image(fetch_poster(top_grossing['movie_id'].values[25]))
        st.write(title(top_grossing, 25))
        st.caption(revenew(25))

    with col27:
        st.image(fetch_poster(top_grossing['movie_id'].values[26]))
        st.write(title(top_grossing, 26))
        st.caption(revenew(26))

    with col28:
        st.image(fetch_poster(top_grossing['movie_id'].values[27]))
        st.write(title(top_grossing, 27))
        st.caption(revenew(27))

    with col29:
        st.image(fetch_poster(top_grossing['movie_id'].values[28]))
        st.write(title(top_grossing, 28))
        st.caption(revenew(28))

    with col30:
        st.image(fetch_poster(top_grossing['movie_id'].values[29]))
        st.write(title(top_grossing, 29))
        st.caption(revenew(29))

    # ------------ Seventh Row-------------#

    col31, col32, col33, col34, col35 = st.columns(5, gap="small")

    with col31:
        st.image(fetch_poster(top_grossing['movie_id'].values[30]))
        st.write(title(top_grossing, 30))
        st.caption(revenew(30))

    with col32:
        st.image(fetch_poster(top_grossing['movie_id'].values[31]))
        st.write(title(top_grossing, 31))
        st.caption(revenew(31))

    with col33:
        st.image(fetch_poster(top_grossing['movie_id'].values[32]))
        st.write(title(top_grossing, 32))
        st.caption(revenew(32))

    with col34:
        st.image(fetch_poster(top_grossing['movie_id'].values[33]))
        st.write(title(top_grossing, 33))
        st.caption(revenew(33))

    with col35:
        st.image(fetch_poster(top_grossing['movie_id'].values[34]))
        st.write(title(top_grossing, 34))
        st.caption(revenew(34))

    # ------------ Eight Row-------------#

    col36, col37, col38, col39, col40 = st.columns(5, gap="small")

    with col36:
        st.image(fetch_poster(top_grossing['movie_id'].values[35]))
        st.write(title(top_grossing, 35))
        st.caption(revenew(35))

    with col37:
        st.image(fetch_poster(top_grossing['movie_id'].values[36]))
        st.write(title(top_grossing, 36))
        st.caption(revenew(36))

    with col38:
        st.image(fetch_poster(top_grossing['movie_id'].values[37]))
        st.write(title(top_grossing, 37))
        st.caption(revenew(37))

    with col39:
        st.image(fetch_poster(top_grossing['movie_id'].values[38]))
        st.write(title(top_grossing, 38))
        st.caption(revenew(38))

    with col40:
        st.image(fetch_poster(top_grossing['movie_id'].values[39]))
        st.write(title(top_grossing, 39))
        st.caption(revenew(39))
