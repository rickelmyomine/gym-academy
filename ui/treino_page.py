import streamlit as st
import pandas as pd
from providers.data_manager import carregar_treino, salvar_treino

def mostrar_pagina_treino():
    st.title("🏋️ Minha Rotina de Treino")
    
    df_treino = carregar_treino()

    # Adicionar Exercício
    st.header("Adicionar Novo Exercício")
    with st.form("form_novo_exercicio", clear_on_submit=True):
        exercicio = st.text_input("Nome do Exercício")
        
        col1, col2 = st.columns(2)
        with col1:
            series = st.number_input("Séries", min_value=1, step=1)
        with col2:
            repeticoes = st.number_input("Repetições", min_value=1, step=1)
            
        link_video = st.text_input("Link do Vídeo (YouTube)")
        submit = st.form_submit_button("Salvar no Treino")
        
        if submit:
            if exercicio != "":
                novo_dado = pd.DataFrame({
                    "Exercício": [exercicio],
                    "Séries": [series],
                    "Repetições": [repeticoes],
                    "Link do Vídeo": [link_video]
                })
                df_treino = pd.concat([df_treino, novo_dado], ignore_index=True)
                salvar_treino(df_treino) # Usa a função do provider
                st.success(f"{exercicio} adicionado com sucesso!")
                st.rerun()
            else:
                st.warning("Por favor, digite o nome do exercício.")

    st.divider()

    # Visualizar, Assistir e Excluir
    st.header("Meu Treino Atual")

    if not df_treino.empty:
        st.dataframe(df_treino, use_container_width=True, hide_index=True)
        st.divider()

        # Remover Exercício
        st.subheader("🗑️ Remover Exercício")
        col_del1, col_del2 = st.columns([3, 1])
        
        with col_del1:
            exercicio_remover = st.selectbox("Selecione o que deseja excluir:", df_treino["Exercício"], label_visibility="collapsed")
        
        with col_del2:
            if st.button("Excluir", use_container_width=True):
                df_treino = df_treino[df_treino["Exercício"] != exercicio_remover]
                salvar_treino(df_treino)
                st.rerun()

        st.divider()

        # Ver Vídeo
        st.subheader("🎥 Ver Execução")
        exercicio_selecionado = st.selectbox("Escolha um exercício para ver o vídeo:", df_treino["Exercício"])
        link_selecionado = df_treino.loc[df_treino["Exercício"] == exercicio_selecionado, "Link do Vídeo"].values[0]
        
        if pd.notna(link_selecionado) and link_selecionado != "":
            st.video(link_selecionado)
        else:
            st.info("Nenhum vídeo cadastrado para este exercício.")
            
    else:
        st.info("Seu treino está vazio. Adicione seus primeiros exercícios acima!")