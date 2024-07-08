import streamlit as st




df_data = st.session_state["data"]


clubes =  df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)



player_status = df_data[df_data["Name"] == player].iloc[0]

st.image(player_status["Photo"])
st.title(player_status["Name"])

st.markdown(f"**Clube:** {player_status['Club']}")
st.markdown(f"**Posição:** {player_status['Position']}")


col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Idade:** {player_status['Age']}")
col2.markdown(f"**Altura:** {player_status['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_status['Weight(lbs.)']*0.453:.2f}")
st.divider()


st.subheader(f"Overall {player_status['Overall']}")
st.progress(int(player_status["Overall"]))


col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_status['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_status['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_status['Release Clause(£)']:,}")