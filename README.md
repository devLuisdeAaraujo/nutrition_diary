# Sistema de Diário de nutrição com Machine Learning (Python + SKlearn + MongoDB + Pandas)

Este projeto é uma aplicação web desenvolvida com **Python** e **SKlearn**, com objetivo de realizar **cadastro de refeições** com **manipulação de proteínas e carboidratos com Machine Learning**. Os dados são armazenados em um banco de dados **MongoDB**, com foco em fazer a manipulação do dados cadastrados e **Pandas** para a criação de DataFrame com tabelas.

---

##  Funcionalidades

- Cadastro de refeição (Refeição(Café da manhâ,Almoço ou Jantar),Data, Horário, alimento e quantidade(em g) *Precisa ser em gramas(g) para ter mais precisão.*
- Manipulação dos dados cadastrados **MongoDB**
- Machine Learning **SKlearn**:
- **LinearRegression** para poder utilizar regressão linear para realizar as previsões;
- **Preprocessing** 
- 


---

##  Tecnologias utilizadas

- Python
- Streamlit
- SQLite3
- smtplib (SMTP)
- secrets
- hashlib

---

## Como rodar o projeto localmente

**Pré-requisitos:**  
Python instalado na máquina e biblioteca Streamlit.
## **Estrutura dos arquivos principais:**
 - cadastre.py -> Tela de cadastro de usuários.
 - login.py -> Tela de login dos usuários
 - funcao_token.py -> Geração de código/ token de verificação.
 - token_email.py -> Envio de e-mail com o código via **SMTP**
 - funcao_email_recente.py -> Verificação do código/ token enviado
 - cadastre_user.db -> Banco de dados **SQLITE3** (gerado automaticamente ao rodar)
 - 

### Instalar o Streamlit:

```bash
pip install streamlit
```

## -PASSO 1: Fazendo a aplicação web:
```bash
streamlit run cadastre.py
```
Neste tela você conseguirá fazer o cadastro na página: Cadastrando seu nome de usuário, seu e-mail o qual vai receber o código , seu cpf *Precisa ser cpf verídico*, sua senha *Senha vai ser criptografada dentro do banco de dados utilizando a biblioteca hashlib*. Após isso cadastrá-lo clicando no botão.

## -PASSO 2: Redirecionamento para verificação e-mail:

Após o cadastro, entrará para a página de validação.
```bash
streamlit run token_email.py
```
Nela um código no e-mail cadastrado será enviado, e adicione esse código para verificar a veracidade.

## -PASSO 3: Realizando login:
Após a validação você pode fechar o web já aberto no seu terminal e reabrir usando
```bash
streamlit run login.py
```
Nele fará o login com NOME ou E-MAIL ou CPF,  já cadastrado no Banco de dados, juntamente com sua senha cadastrada.

Caso errar em algo aparecerá a tela.
Se realizar o login corretamente, aparecerá **login concluído com sucesso**.

## -Observações:

-O envio de e-mails está configurado inicialmente para Gmail, mas pode ser adaptado para outros servidores.
-As senhas são **criptografadas** antes de serem armazenadas, aumentando a segurança do sistema.
-Caso queira testar com outro e-mail, é necessário alterar as configurações de **SMTP** no código.

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







