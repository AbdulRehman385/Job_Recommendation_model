# Job Recommender System

This project is a **Job Recommender System** built using collaborative filtering. Given a user's skill, the model recommends job roles relevant to that skill based on collaborative filtering principles.

## Overview

The system is designed to suggest jobs that align with a user’s skills, aiding users in finding suitable job roles efficiently. The collaborative filtering model leverages similarities across skills and jobs, providing personalized recommendations.

## Data Source

The dataset used for building this model is sourced from [Kaggle](https://www.kaggle.com/), containing information on various skills and the associated jobs. This data is cleaned and processed to optimize the recommendation engine’s performance.

## Project Workflow

1. **Data Preprocessing**: The data is cleaned and prepared to remove any inconsistencies.
2. **Model Training**: A collaborative filtering approach is applied to match skills with relevant job roles.
3. **Recommendation**: The model takes a skill as input and recommends jobs related to that skill.

## How to Use the Recommender System

1. **Input a Skill**: The user provides a specific skill (e.g., "Python").
2. **Get Job Recommendations**: The model returns job roles that align with the provided skill.

## Dependencies

The project requires the following libraries:

```text
streamlit==1.39.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.2
```

## APP
APP URL: https://jobrecommendationmodel-sbcn53s5vpdpzwckgg2yiy.streamlit.app/
