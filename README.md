# Sistema de Diário de Nutrição com Machine Learning (Python + Scikit-learn + MongoDB + Pandas)

Este projeto é uma aplicação web desenvolvida com **Python**, utilizando **Streamlit** como interface, com o objetivo de cadastrar refeições e aplicar **Machine Learning** para prever e analisar dados nutricionais como **quantidade de proteínas e carboidratos**.

Os dados são armazenados em um banco **MongoDB**, manipulados com **Pandas**, e o modelo de ML utiliza **Scikit-learn** com `LinearRegression`, `OneHotEncoder`, `ColumnTransformer` e `Pipeline`.

---


---

##  Funcionalidades

- Cadastro de refeição (Refeição(Café da manhâ,Almoço ou Jantar),Data, Horário, alimento e quantidade(em g) *Precisa ser em gramas(g) para ter mais precisão.*
- Manipulação dos dados cadastrados **MongoDB**
- Machine Learning **SKlearn**:
- **LinearRegression** para poder utilizar regressão linear para realizar as previsões;
- **Preprocessing com OneHotEnconder** Ele vai fazer o pré-processamento do código e com OneHotEnconder vai transformar (refeicao/alimento) os dados em opção binária;
- **Compose com ColumnTransformer** Aplica-se nas colunas categóricas;
- **Pipeline** Encadear o pré-modelo de regressão.


---

##  Tecnologias utilizadas

- Python
- Streamlit
- MongoDB
- SKlearn
- Pandas


---

## Como rodar o projeto localmente

**Pré-requisitos:**  
Python instalado na máquina e biblioteca Streamlit.
## **Estrutura dos arquivos principais:**
 - cadastro_refeicao.py -> Tela de cadastro de refeições.
 - tabela.py -> Tela com dados na tabela.

##Criar conexão com o MongoDB
![image](https://github.com/user-attachments/assets/710b309e-1bc3-45b8-a666-87fd722b364e)


### Instalar o Streamlit:

```bash
pip install streamlit
```

## -PASSO 1: Fazendo a aplicação web:
```bash
streamlit run cadastro_refeicao.py
```
Neste tela você conseguirá fazer o cadastro da refeição na página: Cadastrando horário da refeição(Café-da-manhã,Almoço,Jantar), o horário que está realizando a refeição, Tipo de alimento, o alimento e sua quantidade em Gramas(g). Após isso, enviando os dados ao banco de dados MongoDB.

## -PASSO 2: Vizualização dos dados com os aplicados pelo Machine Learning:


```bash
streamlit run tabela.py
```
##- Como funciona:


Mostrará a tabela com as refeições cadastradas e seus carboidratos e suas proteínas de acordo com a quantidade cadastrada.
![image](https://github.com/user-attachments/assets/eb8d85b1-c510-47df-9916-03c4b9a34fad)

Primeiramente, crio um arquivo com valores em forma de dicionário para ser percorrido de acordo com seus valores.
![image](https://github.com/user-attachments/assets/d98fce1f-456b-46fd-8cb2-0c5ff77e413c)

Faço a criação data- X e o target- Y, no qual no X passo um OneHotEnconder para poder transformar as opções em binário. Com o pipeline faço a pré-processamento indiciando X,y para treinar o modelo(.fit()).

![image](https://github.com/user-attachments/assets/8ac41514-b882-4bfe-a325-8d7a6b96e247)

Passo que de acordo com 100 gramas ele utilizará os valores que eu passei na __init__ para poder fazer a comparação e com isso fazer a multiplicação com a quantidade cadastrada no Banco de dados.

Com esse projeto consigo iniciar meus estudos com Machine Learning, aprendendo sobre Regressão Linear, tipos de classificações(RBF,Polinomio,classe linearmente separada), SVM´S Kernels, Acurácias.

## -Contate-me:

**E-mail**
```bash
E-mail: luis.araujo.sesisenaisp@gmail.com
````
**Telefone**
```bash
+55 (11) 97470-0738
```
**Instagram**
```bash
@l.gustazz
```







