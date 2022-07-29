# Spotify-Classification-Recommendation-System

Checkout the notebook [here](https://alif898.github.io/Spotify-Classification-Recommendation-System/)!

Note: Unfortuantely, some of the outputs are rendered in full instead of a smaller scrollable window, which makes it trickier to read. This seems to be a limitation of the way it was written on Databricks. For the best viewing experience, you may try to run the notebook on your own Databricks account.

## Introduction

As an avid-user of spotify and a big fan of music in general, I have always been curious about 2 things:

1. What makes certain songs popular? Is there a way to quantify and even predict what makes songs popular?
2. How does the Spotify recommendation algorithm work? Under the 'Made for You' section, there are a multitude of curated playlists based on genres, artists and even moods. I have managed to discover a plethora of artists and songs through these playlists that I would not have known about otherwise, yet it can sometimes feel very hit-or-miss.

I then realised that Spotify has an API that allows us to fetch information about tracks, artists, playlists and I thought it would be interesting to answer the above 2 questions.

This project will be split into the following parts:
1. Methodology
2. Data Engineering - ETL pipeline to fetch data from Spotify API into Delta Lake
3. EDA
4. Regression model to predict track popularity
5. Classification model to recommend songs
6. Conclusion

## Design

Requirements:
- Databricks account (The notebook was run on Databricks Community Edition)
- Spotify Developer account

![diagram](https://github.com/alif898/Spotify-Classification-Recommendation-System/blob/main/diagram.png?raw=true)

In summary, user playlist track data is fetched through the Spotify API and transformed with PySpark, before being loaded into Delta Lake. Susbequently, we take this data and build our machine learning models, again with PySpark and its ML library, pyspark.ml. Model performance is tracked with MLflow. All of this is done through a Databricks notebook.

Full notebook: [link](https://alif898.github.io/Spotify-Classification-Recommendation-System/)
