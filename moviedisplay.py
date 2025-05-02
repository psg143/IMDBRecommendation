import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
import time


st.set_page_config(layout='wide')

# Function to recommend movies based on user input and precomputed similarity rankings
def compute_similarity(input_storyline, movies_df):
    # Combine input storyline with existing storylines
    storylines = movies_df['Cleaned_Storyline'].tolist()
    storylines.insert(0, input_storyline)  # Add user input at the beginning

    # Compute TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(storylines)

    # Compute cosine similarity
    similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])[0]

    # Add similarity scores to the dataframe
    movies_df['Similarity_Score'] = similarity_scores
    
    filtered_df = movies_df[movies_df['Similarity_Score'] > 0]

    top_movies = filtered_df.sort_values(by='Similarity_Score', ascending=False).head(5)
    top_similarity_scores = top_movies['Similarity_Score'].tolist()
    top_movies_list = top_movies['MovieName'].tolist()
    return top_movies, top_movies_list, top_similarity_scores


# Bar plot for similarity scores
def plot_similarity(similarity_scores, movie_names):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=similarity_scores, y=movie_names, palette="viridis")
    plt.title("Similarity Scores for Recommended Movies")
    plt.xlabel("Similarity Score")
    plt.ylabel("Movie Name")
    st.pyplot(plt)

@st.cache_data
def loadcsvdata(filename): 
    return pd.read_csv(filename)

# Show a spinner during a process
with st.spinner(text='In progress', show_time=True):
    movies_df = loadcsvdata("movie_vector_data.csv") 
    movies_df['Cleaned_Storyline'] = movies_df['Cleaned_Storyline'].fillna("")

    st.title("🎬 Movie Recommendation System")
    st.write("Find the top 5 recommended movies based on your storyline input!")

    # Three columns with different widths
    col1, col2, col3 = st.columns([3,1,1])
    # col1 is wider

    # Using 'with' notation:
    with col1: 
        user_storyline = st.text_area("Enter a movie storyline:", placeholder="Write a short storyline or description...")
 
    if st.button("Find Recommendations"):
        if user_storyline.strip():
            
            # Show and update progress bar
            bar = st.progress(0)

            top_movies, top_movies_list, top_similarity_scores = compute_similarity(user_storyline, movies_df)
            bar.progress(25)

            if sum(top_similarity_scores) > 0:
                # Display recommendations
                st.write("### Top 5 Recommended Movies:")

                col1, col2, col3 = st.columns([2,2,2], border=False)

                drowindex=0
                for i, row in top_movies.iterrows():
                    if(i<=75):
                        bar.progress(25+i)
                    # st.write(f"**{row['MovieName']}**")
                    # st.write(f"*Storyline*: {row['StoryLine']}")
                    # st.write("---")

                    if(drowindex==0 or drowindex==3):
                        with col1:
                            container = st.container(border=True)  
                            container.markdown(f"""
                            <h3 style='font-size: 24px;'><b>{row['MovieName']}</b></h3>
                            """, unsafe_allow_html=True)
                            container.write(f"*Storyline*: {row['StoryLine']}")  
                            # st.write("---")
                    if(drowindex==1 or drowindex==4):
                        with col2:
                            container = st.container(border=True)  
                            container.markdown(f"""
                            <h3 style='font-size: 24px;'><b>{row['MovieName']}</b></h3>
                            """, unsafe_allow_html=True)
                            container.write(f"*Storyline*: {row['StoryLine']}")  
                    if(drowindex==2):
                        with col3:
                            container = st.container(border=True)  
                            container.markdown(f"""
                            <h3 style='font-size: 24px;'><b>{row['MovieName']}</b></h3>
                            """, unsafe_allow_html=True)
                            container.write(f"*Storyline*: {row['StoryLine']}")  
                        

                    drowindex=drowindex+1
                    
                plot_similarity(top_similarity_scores, top_movies_list)
                st.snow() 
            else:
                st.toast('Oops! No Movies found for given storyline')
                st.info('Oops! No Movies found for given storyline')

            bar.progress(100)
        else:
            st.error("Please enter a storyline to get recommendations!")

        del bar

