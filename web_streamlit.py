import streamlit as st
from pymongo import MongoClient

class Aplicativo:
    def __init__(self):
        st.title("Diário de alimentação")

       
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["nutritiondiary"]
        self.colecao = self.db["cadastre"]

        
        self.frutas = [
            "Banana", "Maçã", "Uva", "Pera", "Laranja", "Abacaxi",
            "Morango", "Manga", "Melancia", "Mamão", "Kiwi",
            "Coco", "Limão", "Framboesa"
        ]

        self.proteinas_cafe_da_manha = [
            "Ovo", "Leite", "Iogurte natural", "Queijo branco (ricota, minas)",
            "Requeijão light", "Peito de peru", "Atum", "Carne de soja", "Tofu",
            "Manteiga de amendoim (sem açúcar)", "Shake proteico (whey protein)", "Cottage"
        ]

        self.carboidratos_cafe_da_manha = [
            "Pão francês", "Pão integral", "Tapioca", "Cuscuz", "Aveia", "Granola",
            "Bolo simples (milho, fubá, etc.)", "Bolacha integral", "Banana (rica em carboidrato)",
            "Batata-doce", "Inhame", "Arroz integral (p/ café reforçado)"
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
                "quantidade": quantidade
            }

            self.colecao.insert_one(dados)
            st.success("Refeição salva com sucesso!")

    def pagina_almoco(self):
        st.subheader("🍽️ Almoço")
        st.write("Aqui você pode registrar o que comeu no almoço.")
        

    def pagina_janta(self):
        st.subheader("🌙 Janta")
        st.write("Aqui você pode registrar o que comeu na janta.")
        

if __name__ == "__main__":
    Aplicativo()
