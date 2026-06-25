import streamlit as st
import pandas as pd
from providers.data_manager import carregar_treino, carregar_cronograma, salvar_cronograma

def mostrar_pagina_cronograma():
    st.title("📅 Meu Cronograma da Semana")

    # Carrega os dados
    df_treino = carregar_treino()
    df_crono = carregar_cronograma()

    if df_treino.empty:
        st.warning("Você precisa adicionar exercícios na 'Área de Treino' antes de montar o cronograma!")
        return

    lista_exercicios = df_treino["Exercício"].tolist()
    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

    # 1. Adicionar ao Cronograma
    st.header("Montar Treino do Dia")
    
    with st.form("form_cronograma"):
        dia_selecionado = st.selectbox("Escolha o Dia:", dias_semana)
        exercicios_selecionados = st.multiselect("Quais exercícios você fará neste dia?", lista_exercicios)

        if st.form_submit_button("Salvar no Cronograma"):
            if exercicios_selecionados:
                exercicios_str = ", ".join(exercicios_selecionados)
                
                # Remove o treino anterior desse dia (se existir)
                df_crono = df_crono[df_crono["Dia da Semana"] != dia_selecionado]
                
                # Adiciona o novo
                novo_dado = pd.DataFrame({"Dia da Semana": [dia_selecionado], "Exercícios": [exercicios_str]})
                df_crono = pd.concat([df_crono, novo_dado], ignore_index=True)

                # Ordena a tabela pelos dias da semana
                df_crono['Dia da Semana'] = pd.Categorical(df_crono['Dia da Semana'], categories=dias_semana, ordered=True)
                df_crono = df_crono.sort_values('Dia da Semana')

                salvar_cronograma(df_crono)
                st.success(f"Treino de {dia_selecionado} salvo com sucesso!")
                st.rerun()
            else:
                st.warning("Selecione pelo menos um exercício para salvar.")

    st.divider()

    # 2. Visualização do Cronograma
    st.header("Resumo da Semana")
    
    if not df_crono.empty:
        # Mostra os dias salvos
        for index, row in df_crono.iterrows():
            st.subheader(f"🗓️ {row['Dia da Semana']}")
            st.write(f"**Treino:** {row['Exercícios']}")
            st.write("---")
            
        st.divider()
        
        # 3. Remover um Dia do Cronograma
        st.subheader("🗑️ Limpar Dia do Cronograma")
        col_del1, col_del2 = st.columns([3, 1])
        
        with col_del1:
            dia_remover = st.selectbox("Selecione o dia para limpar:", df_crono["Dia da Semana"], label_visibility="collapsed")
        
        with col_del2:
            if st.button("Limpar Dia", use_container_width=True):
                # Filtra o dataframe removendo o dia selecionado
                df_crono = df_crono[df_crono["Dia da Semana"] != dia_remover]
                salvar_cronograma(df_crono)
                st.rerun()
                
    else:
        st.info("Seu cronograma está vazio. Comece a planejar sua semana no formulário acima!")