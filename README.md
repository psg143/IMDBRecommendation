# IMDb 2024 Data Scraping and Visualizations

## Overview
This project focuses on extracting movie data from IMDb for 2024, specifically targeting movie names and their storylines. The goal is to build a recommendation system that suggests similar movies based on a given storyline.

## Features
- **Data Scraping**: Use Selenium to scrape IMDb for movie names and their associated storylines.
- **Natural Language Processing (NLP)**: Pre-process and analyze storylines using techniques like:
    - TF-IDF (Term Frequency-Inverse Document Frequency)
    - Count Vectorizer
- **Recommendation System**: Calculate Cosine Similarity or apply Machine Learning algorithms to recommend similar movies.
- **Interactive User Interface**: Built with Streamlit, allowing users to input a storyline and receive the top 5 recommended movies.

## Technologies Used
- **Python**: Core programming language.
- **Selenium**: For web scraping IMDb data.
- **NLP Libraries**: Scikit-learn, NLTK, or SpaCy for text processing and analysis.
- **Streamlit**: For building the user interface.
- **Machine Learning**: Algorithms for similarity calculation and recommendations.

## How It Works
1. **Data Collection**: Scrape IMDb for movie names and storylines using Selenium.
2. **Data Preprocessing**: Clean and tokenize the storylines for analysis.
3. **Feature Extraction**: Use TF-IDF or Count Vectorizer to represent the storylines numerically.
4. **Similarity Calculation**: Compute Cosine Similarity or use ML algorithms to find similar movies.
5. **User Interaction**: Provide recommendations through a Streamlit-based interface.

## Usage
1. Run the Streamlit application:
     ```bash
     streamlit run moviedisplay.py
     ```
2. Input a movie storyline in the interface.
3. View the top 5 recommended movies based on the input storyline.

## Future Enhancements
- Expand the dataset to include additional movie attributes (e.g., genres, ratings, image).
- Incorporate advanced NLP techniques like BERT for better recommendations.
- Add support for multilingual storylines.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- IMDb for providing the movie data.
- Open-source libraries and tools used in this project.
