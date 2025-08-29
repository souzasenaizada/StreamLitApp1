import streamlit as st
import pandas as pd
from database import criar_tabela, inserir_funcionario, listar_funcionarios

# Criar tabela ao iniciar
criar_tabela()

st.set_page_config(page_title="cadastro de Funcionarios", page_icon="")

st.title("Cadastro de Funcionarios")

# Formulário para adicionar funcionário
with st.form("form_funcionario", clear_on_submit=True):
    nome = st.text_input("nome")
    cargo = st.text_input("cargo")
    email = st.text_input("email")
    
    submit = st.form_submit_button("adicionar")

    if submit:
        if nome and cargo and email:
            try:
                inserir_funcionario(nome,cargo,email)
                st.success(f"Funcionario {nome} adicionado!")
            except Exception as e:
                st.error(f"Erro:{e}")
        else:
            st.warning("Preencha todos os campos!")
st.subheader("Lista de Funcionarios")                     


# Exibir os funcionários cadastrados
dados = listar_funcionarios()
if dados:
    df = pd.DataFrame(dados, columns=["ID", "Nome", "Cargo", "Email"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("Nenhum funcionário cadastrado ainda.")
                
