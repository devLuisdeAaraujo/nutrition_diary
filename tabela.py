import streamlit as st
from pymongo import MongoClient
import pandas as pd


class Utilidades:
    def __init__(self):
        self.title_utilidades = st.title("🍽 Tabela de refeições")
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["nutritiondiary"]
        self.colecao = self.db["cadastre"]
    def mostrar_tabela_de_refeicao(self):
        dados = list(self.colecao.find({},{'_id':0}))
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df,use_container_width=True)
        else:
            st.info("Nenhuma refeição cadastrada")
        

if __name__ == "__main__":
    Utilidades().mostrar_tabela_de_refeicao()





        

    