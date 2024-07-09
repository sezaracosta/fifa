import streamlit as st
#biblioteca para linkar paginas web
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    #lendo o arquivo csv - primeira coluna do csv será usada  como índece
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)

   #filtra os dados da coluna "Contract Valid Unitil" para que apresenta apenas as tem que um valor igual ou maior do que o ano atual
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
  
   # para apresentar apenas os valores maiores que zero referente a essa coluna
    df_data = df_data[df_data["Value(£)"] > 0]

    #ordenando os dados pela conula "Overall", ordenando por ordem cresente
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