# a tool for a user to get a summary of Wikipedia movie data.

# dependencies
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# helper functions
def dict_moviesbygenre( wiki_df ):
    """
    dict_moviesbygenre iterates over a df to generate dict 
    the dict's keys are the genres
    the dict's values are movie titles
    """
    res_dict = {}
    for index, row in wiki_df.iterrows():
        if row['genres']:
            for genre in row['genres']:
                if genre not in res_dict.keys():
                    res_dict[genre]=[]
                res_dict[genre].append(row['title'])
    return res_dict

def dict_actbygenre( wiki_df ):
    """
    dict_actbygenre iterates over a df to generate dict 
    the dict's keys are the genres
    the dict's values are movie titles
    """
    res_dict = {}
    for index, row in wiki_df.iterrows():
        if row['genres']:
            for genre in row['genres']:
                if genre not in res_dict.keys():
                    res_dict[genre]=[]
                for act in row['cast']:
                    if act not in res_dict[genre]:
                        res_dict[genre].append(act)  
    return res_dict

def format_genreplot_df( genre_dict ):
    """
    helper function to return a df formatted to plot
    genre distributions
    """
    genres = list(genre_dict.keys())
    counts = list(genre_dict.values())
    counts = [len(l) for l in counts]
    plot_dict = {'Genres':genres,'Counts':counts}
    genres_df = pd.DataFrame(plot_dict)
    return genres_df

def main():
    # Step 1: import the data as a pandas df¶
    json_path = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json'
    df = pd.read_json(json_path)

    st.title( 'WikiMovies Exploration Tool' )
    st.write('***' )
    st.markdown( '### Wikipedia Movies per Year')

    col1, col2 = st.columns(2)

    with col1:
        st.write('A scrollable table with the number of yearly movie releases')
        # Step 2 Generate a table showing the number of movies made in each year.
        yearly_df = df['year'].value_counts().sort_index().reset_index().rename(columns={"index": "Year", "year": "Count"})
        yearly_df.style

    with col2:
        st.write('')
        st.write('')
        st.write('')
        fig1 = plt.figure(figsize=(5,5))
        sns.lineplot(data=yearly_df, x="Year", y="Count").set(title='Yearly Movie Releases')
        plt.ylabel("Number of Movies")
        sns.despine()
        st.pyplot( fig1 )

    st.write('***' )
    # Step 3: Generate a dictionary which maps each genre to a list of movies. 
    # You can ignore the movies with missing genres.
    st.markdown( '### Wikipedia Movies by Genre')  

    genre_dict_movies = dict_moviesbygenre( df )
    genre_movies_plt = format_genreplot_df( genre_dict_movies )

    col1, col2 = st.columns(2)

    with col1:
        st.write('A scrollable table with the number of movies per genre')
        genre_movies_plt.style
    with col2:
        fig2 = plt.figure(figsize=(5,7))
        ax = sns.barplot(x="Counts", y="Genres", data=genre_movies_plt).set(title='Number of Movies by Genre')
        st.pyplot( fig2 )

    genres = list(genre_dict_movies.keys())
    default_ix = genres.index('Martial Arts')
    selected_moviesgenre = st.selectbox('Select a movie genre:', genres, index=default_ix)
    st.write( genre_dict_movies[selected_moviesgenre])

    st.write('***' )
    # Step 4: Find all actors/actresses who were in a 2018 drama movie.
    # (Spark implementation done outside of this app)
    st.markdown( '### Wikipedia Actors & Actresses by Genre')

    years = df['year'].unique().tolist()
    default_yearix = years.index(2018)
    selected_yeargenre = st.selectbox('Select a movie release year:', years, index=default_yearix)
    df_sub = df[df['year']==selected_yeargenre]

    genre_dict_act = dict_actbygenre( df_sub )
    genre_act_plt = format_genreplot_df( genre_dict_act )

    genres2 = list(genre_dict_act.keys())
    default_ix2 = genres2.index('Drama')
    selected_actgenre = st.selectbox('Select a movie genre:', genres2, index=default_ix2)

    col1, col2 = st.columns(2)

    with col1:
        st.write('A scrollable table with the number of actors & actresses per genre')
        genre_act_plt.style  
    with col2:
        st.write('View actors & actresses for selected genre & year')
        st.write( genre_dict_act[selected_actgenre])


if __name__ == '__main__':
    main()