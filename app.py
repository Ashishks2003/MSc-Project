import streamlit as st
import pandas as pd

df = pd.read_csv('player_stats_with_improvement_plans.csv')

st.title("Cricket Player Batting Analytics & Improvement Plans")

player_ids = df['player_ID']
cluster_ids = df['cluster_id'].unique()

st.sidebar.header("Player & Cluster Search")
select_mode = st.sidebar.radio("Choose search mode:", ['Player ID', 'Cluster'])

if select_mode == 'Player ID':
    player_selected = st.sidebar.selectbox("Select Player ID:", player_ids)
    player = df[df['player_ID']==player_selected].iloc[0]
    st.subheader(f"Player Profile: {player_selected}")
    st.write('**Cluster:**', int(player['cluster_id']))
    st.write('**Total Runs:**', int(player['total_runs']))
    st.write('**Balls Faced:**', int(player['balls_faced']))
    st.write('**Dismissals:**', int(player['dismissals']))
    st.write('**Strike Rate:**', round(player['strike_rate'],2))
    st.write('**Improvement Plan:**', player['improvement_plan'])

elif select_mode == 'Cluster':
    cluster_selected = st.sidebar.selectbox("Select Cluster:", cluster_ids)
    cluster_players = df[df['cluster_id']==cluster_selected]
    st.subheader(f"Cluster {int(cluster_selected)} Overview")
    st.write(f"Number of Players: {cluster_players.shape[0]}")
    st.dataframe(cluster_players[['player_ID','total_runs','strike_rate','improvement_plan']].reset_index(drop=True))
    st.write("Typical Improvement Plan for This Cluster:")
    st.write(cluster_players['improvement_plan'].iloc[0])

    if st.checkbox("Show cluster summary statistics"):
        st.write(cluster_players.describe())
