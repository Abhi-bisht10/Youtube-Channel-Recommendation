import streamlit as st
import pandas as pd
import pickle

channel_dict = pickle.load(open('channel_dict.pkl','rb'))
channel = pd.DataFrame(channel_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(channels):
    channel_index = channel[channel['Youtuber'] == channels].index[0]
    distances = similarity[channel_index]
    channel_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_channel = []

    for i in channel_list:
        recommended_channel.append(channel.iloc[i[0]].Youtuber)
    return recommended_channel

st.title('Youtube Recommender System')

selected_channel = st.selectbox(
    'Select the Youtube Channel',
    channel['Youtuber'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_channel)
    for i in recommendations:
        st.write(i)
