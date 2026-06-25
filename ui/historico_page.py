import streamlit as st
from providers.data_manager import carregar_historico

def mostrar_pagina_historico():
    st.title("🏆 Meu Histórico de Treinos")
    st.write("Acompanhe sua consistência ao longo do tempo!")

    df_hist = carregar_historico()

    if not df_hist.empty:
        # Cria um card visual mostrando o total de treinos que você já fez
        st.metric(label="Total de Treinos Concluídos", value=len(df_hist))
        
        st.divider()
        st.subheader("Registro Diário")
        st.dataframe(df_hist, use_container_width=True, hide_index=True)
    else:
        st.info("Você ainda não concluiu nenhum treino. Vá para o 'Modo Treino', complete seus exercícios e salve seu primeiro registro!")