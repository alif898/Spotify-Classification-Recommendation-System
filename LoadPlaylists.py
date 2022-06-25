# Importing required packages
from __future__ import annotations
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set, directory filename and playlist name here
directory = r'C:\Users\XXX'
next_df = pd.read_csv(directory + r'/' + 'XXX')
next_playlist_name = 'XXX'

# Spotify API Login Details
client_id = 'XXX'
client_secret = 'XXX'
# Username to create playlist for
username = 'XXX'
scope = 'playlist-modify-public'
# The redirect location set in your Spotify Developer acccount
redirect_uri = 'http://localhost:8888/callback/'

auth_manager = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)
#token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

def create_playlists(df: pandas.DataFrame, name : str) -> None:
    """
    Function that takes in a DataFrame of tracks and uploads them to new Spotify playlist
    
    * df: DataFrame containing tracks to upload
    * name: Name of playlist to be created
    """
    tracks = df['track_uri'].tolist()
    playlist = sp.user_playlist_create(username, name)
    playlist_uri = playlist['id']
    
    # Spotify API only allows addition of 100 tracks per request
    for i in range(0, len(tracks), 100):
        next_batch = tracks[i:i + 100]
        sp.user_playlist_add_tracks(username, playlist_uri, tracks=next_batch)

create_playlists(next_df, next_playlist_name)            