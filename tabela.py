import streamlit as st
from pymongo import MongoClient
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class Utilidades:
    def __init__(self):
        self.title_utilidades = st.title("🍽 Tabela de refeições")
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["nutritiondiary"]
        self.colecao = self.db["cadastre"]
        self.dados_ml = pd.DataFrame({
        "Alimento": ["Ovo", "Banana","Leite","Pão Integral","Maça","Uva","Iogurte natural","Shake proteico (whey protein)","Pão Frances","Tapioca","Picanha","Contrafile","Patinho","Arroz","Macarrão","Batata Frita","Frango Assado","Salmão Grelhado","Ovo","Arroz","Feijão","Lentilha"],
        "Proteina": [13,1.3,3.3,9.5,0.36,0.6,5.25,86.58,4.00,0.7,19.72,24,21.75,2.66,5.76,5.1,28,26.1,13,2.66,4.8,6.3],
        "Carboidrato":[1.1,23,4.8,40,25,18,7.4,1.22,29.45,36,0,0,0,27.9,30.68,35.6,0,0,1.1,27.9,5.1,16.3]
        })
        self.modelo = self.treinar_modelo()
    
    def treinar_modelo(self):
        X = pd.DataFrame({
            "Alimento":self.dados_ml["Alimento"],
            "Quantidade":[100]*len(self.dados_ml)
        })
        y=self.dados_ml[["Proteina","Carboidrato"]]
        preprocessor = ColumnTransformer(transformers=[
            ("onehot",OneHotEncoder(),["Alimento"])
        ],remainder="passthrough")

        pipeline = Pipeline(steps=[
            ("preprocessador",preprocessor),
            ("regressor",LinearRegression())
        ])
        pipeline.fit(X,y)
        return pipeline
    def prever_nutrientes(self,alimento,quantidade):
        entrada = pd.DataFrame([{"Alimento":alimento, "Quantidade":100}])
        try:
            resultado = self.modelo.predict(entrada)
            fator = quantidade/100
            proteina = round(resultado[0][0]* fator,2)
            carboidrato = round(resultado[0][1]*fator,2)
        except:
            proteina = carboidrato = None
        return proteina,carboidrato

    
    def mostrar_tabela_de_refeicao(self):
        dados = list(self.colecao.find({},{'_id':0}))
        if dados:
            df = pd.DataFrame(dados)
            proteinas_previstas = []
            carboidratos_previstos = []

            for _, row in df.iterrows():
                alimento = row.get("alimento")
                quantidade = row.get("quantidade/g", 0)
                p, c = self.prever_nutrientes(alimento, quantidade)
                proteinas_previstas.append(p)
                carboidratos_previstos.append(c)

            df["Proteína (g) estimada"] = proteinas_previstas
            df["Carboidrato (g) estimado"] = carboidratos_previstos

            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhuma refeição cadastrada")
        

if __name__ == "__main__":
    Utilidades().mostrar_tabela_de_refeicao()





        

    