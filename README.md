# Spotify-Clasification-Recommendation-System

https://alif898.github.io/Spotify-Clasification-based-Recommendation-System/

### Introduction

As an avid-user of spotify and a big fan of music in general, I have always been curious about 2 things:

1. What makes certain songs popular? Is there a way to quantify and even predict what makes songs popular?
2. How does the Spotify recommendation algorithm work? Under the 'Made for You' section, there are a multitude of curated playlists based on genres, artists and even moods. I have managed to discover a plethora of artists and songs through these playlists that I would not have known about otherwise, yet it can sometimes feel very hit-or-miss.

I then realised that Spotify has an API that allows us to fetch information about tracks, artists, playlists and I thought it would be interesting to answer the above 2 questions.

This project will be split into the following parts:
1. Methodology
2. Data Engineering - ETL Pipeline to fetch data from Spotify API into Delta Lake
3. EDA
4. Regression model to predict track popularity
5. Classification model to recommend songs
6. Conclusion

### System Design

![diagram](https://github.com/alif898/Spotify-Clasification-based-Recommendation-System/blob/main/diagram.png?raw=true)
