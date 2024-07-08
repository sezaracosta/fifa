import streamlit as st
#biblioteca para linkar paginas web
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data



st.markdown("# FIFA23 OFFICIAL DATASET")


#criando botão para acessar os dados do kaggle (quando clicamos no botão ele altera o estado para true e abre o site )
btn = st.button("Acesse os dados do Kaggle")
if btn:
   webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
   """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações
    sobre os jogadores profissionais.

    Com **mais de 17.000 registros** este conjunto de dados oferece um recurso valioso para analistas de futebol.

   """

)