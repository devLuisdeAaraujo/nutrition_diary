import streamlit as st
from pymongo import MongoClient

class Aplicativo:
    def __init__(self):
        st.title("Diário de alimentação")

       
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["nutritiondiary"]
        self.colecao = self.db["cadastre"]

        
        
        self.frutas = [
            "Banana", "Maçã", "Uva"
        ]

        self.proteinas_cafe_da_manha = [
            "Ovo", "Leite", "Iogurte natural",  "Shake proteico (whey protein)"
        ]

        self.carboidratos_cafe_da_manha = [
            "Pão francês", "Pão integral", "Tapioca"
        ]
        self.proteinas_almoco = [
            "Picanha", "Contrafile", "Patinho"
        ]
        self.carboidratos_almoco = [
            "Arroz","Macarrão","Batata Frita"
        ]
        self.proteinas_janta = [
            "Frango Assado", "Salmão Grelhado", "Ovo"
        ]
        self.carboidratos_jantas = [
            "Arroz", "Feijão", "Lentilha"
        ]
        menu = st.radio("Escolha a refeição:", ["Café da Manhã", "Almoço", "Janta"], horizontal=True)

        if menu == "Café da Manhã":
            self.pagina_cafe()
        elif menu == "Almoço":
            self.pagina_almoco()
        elif menu == "Janta":
            self.pagina_janta()

    def pagina_cafe(self):
        st.subheader("☕ Café da Manhã")
        st.write("Aqui você pode registrar o que comeu no café da manhã.")
        data = st.date_input("Data de hoje")
        horario = st.time_input("Horário da alimentação")

        tipos_de_comida = ["🍌 Frutas", "🍗 Proteínas", "🍚 Carboídratos"]
        escolha_alimentacao = st.radio("Selecione um tipo de comida:", tipos_de_comida, horizontal=True)
        st.write(f"Você selecionou: {escolha_alimentacao}")

        alimento_escolhido = None

        if escolha_alimentacao == "🍌 Frutas":
            alimento_escolhido = st.selectbox("Escolha uma fruta:", self.frutas)

        elif escolha_alimentacao == "🍗 Proteínas":
            alimento_escolhido = st.selectbox("Escolha uma proteína:", self.proteinas_cafe_da_manha)

        elif escolha_alimentacao == "🍚 Carboídratos":
            alimento_escolhido = st.selectbox("Escolha um carboidrato:", self.carboidratos_cafe_da_manha)

        quantidade = st.number_input("Quantidade (gramas ou unidades)", step=1)

        if st.button("Salvar refeição"):
            dados = {
                "refeicao": "Café da Manhã",
                "tipo": escolha_alimentacao,
                "data": str(data),
                "horario": str(horario),
                "alimento": alimento_escolhido,
                "quantidade/g": quantidade
            }
            self.colecao.insert_one(dados)
            st.success("Refeição salva com sucesso!")

    def pagina_almoco(self):
        st.subheader("🍽️ Almoço")
        st.write("Aqui você pode registrar o que comeu no almoço.")
        data_almoco = st.date_input("Data de hoje")
        horario_almoco= st.time_input("Horário da alimentação")

        tipos_de_comida = ["🍌 Frutas", "🍗 Proteínas", "🍚 Carboídratos"]
        escolha_alimentacao = st.radio("Selecione um tipo de comida:", tipos_de_comida, horizontal=True)
        st.write(f"Você selecionou: {escolha_alimentacao}")

        alimento_escolhido = None

        if escolha_alimentacao == "🍌 Frutas":
            alimento_escolhido = st.selectbox("Escolha uma fruta:", self.frutas)

        elif escolha_alimentacao == "🍗 Proteínas":
            alimento_escolhido = st.selectbox("Escolha uma proteína:", self.proteinas_almoco)

        elif escolha_alimentacao == "🍚 Carboídratos":
            alimento_escolhido = st.selectbox("Escolha um carboidrato:", self.carboidratos_almoco)

        quantidade = st.number_input("Quantidade (gramas ou unidades)", step=1)

        if st.button("Salvar refeição"):
            dados = {
                "refeicao": "Café da Manhã",
                "tipo": escolha_alimentacao,
                "data": str(data_almoco),
                "horario": str(horario_almoco),
                "alimento": alimento_escolhido,
                "quantidade/g": quantidade
            }
            self.colecao.insert_one(dados)
            st.success("Refeição salva com sucesso!")
        

    def pagina_janta(self):
        st.subheader("🌙 Janta")
        st.write("Aqui você pode registrar o que comeu na janta.")
        data_janta = st.date_input("Data de hoje")
        horario_janta= st.time_input("Horário da alimentação")

        tipos_de_comida = ["🍌 Frutas", "🍗 Proteínas", "🍚 Carboídratos"]
        escolha_alimentacao = st.radio("Selecione um tipo de comida:", tipos_de_comida, horizontal=True)
        st.write(f"Você selecionou: {escolha_alimentacao}")

        alimento_escolhido = None

        if escolha_alimentacao == "🍌 Frutas":
            alimento_escolhido = st.selectbox("Escolha uma fruta:", self.frutas)

        elif escolha_alimentacao == "🍗 Proteínas":
            alimento_escolhido = st.selectbox("Escolha uma proteína:", self.proteinas_janta)

        elif escolha_alimentacao == "🍚 Carboídratos":
            alimento_escolhido = st.selectbox("Escolha um carboidrato:", self.carboidratos_jantas)

        quantidade = st.number_input("Quantidade (gramas ou unidades)", step=1)

        if st.button("Salvar refeição"):
            dados = {
                "refeicao": "Café da Manhã",
                "tipo": escolha_alimentacao,
                "data": str(data_janta),
                "horario": str(horario_janta),
                "alimento": alimento_escolhido,
                "quantidade/g": quantidade
            }
            self.colecao.insert_one(dados)
            st.success("Refeição salva com sucesso!")
        

if __name__ == "__main__":
    Aplicativo()
