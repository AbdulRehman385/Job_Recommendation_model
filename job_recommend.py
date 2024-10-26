import streamlit as st

import pandas as pd
import numpy as np

import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


jobs_df = pickle.load(open(r'jobs_df.pkl', 'rb'))

st.title('Job Recommender system')
cv = CountVectorizer(max_features = 300)

skills_matrix = cv.fit_transform(jobs_df['skills'])

#Recommender function takes skills and give related jobs offers
def recommend_jobs(skills, n_jobs = 5):

  # convert input skills to avector
  input_skills_vector = cv.transform([skills])

  # Find similarity between input vector to a vector matrix

  similarity = cosine_similarity(input_skills_vector, skills_matrix).flatten()

  # finding top related job offers (argsort just gives order numbering)
  top_indices = similarity.argsort()[-n_jobs : ][::-1]

  # Getting the similar job offers whose index are given as top_indices
  similar_jobs = jobs_df['job_title'].iloc[top_indices]

  return similar_jobs

# Defining the architecture of app


skill_input = st.text_input('Enter job skill:')

if st.button('Recommend'):
    jobs_recommended = recommend_jobs(skill_input)
    st.write('Jobs offers:')
    st.write(jobs_recommended)
