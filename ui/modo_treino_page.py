import streamlit as st
import pandas as pd
from datetime import date
from providers.data_manager import carregar_treino, carregar_cronograma, carregar_historico, salvar_historico

def mostrar_pagina_modo_treino():
    st.title("💪 Modo Treino")
    st.write("Selecione o treino de hoje e marque os exercícios concluídos!")

    df_treino = carregar_treino()
    df_crono = carregar_cronograma()

    if df_crono.empty:
        st.warning("Seu cronograma está vazio. Vá até 'Cronograma da Semana' para montar seus dias antes de treinar.")
        return

    dias_com_treino = df_crono["Dia da Semana"].tolist()
    
    st.divider()
    dia_hoje = st.selectbox("Qual é o treino de hoje?", dias_com_treino)

    if dia_hoje:
        exercicios_str = df_crono.loc[df_crono["Dia da Semana"] == dia_hoje, "Exercícios"].values[0]
        lista_exercicios = exercicios_str.split(", ")

        st.subheader(f"🔥 Foco no Treino: {dia_hoje}")
        
        progresso_atual = 0
        total_exercicios = len(lista_exercicios)

        for exercicio in lista_exercicios:
            concluido = st.checkbox(f"**{exercicio}**", key=f"check_{exercicio}")
            
            if concluido:
                progresso_atual += 1
                
            link_video = df_treino.loc[df_treino["Exercício"] == exercicio, "Link do Vídeo"].values
            if len(link_video) > 0 and str(link_video[0]) != "nan" and str(link_video[0]).strip() != "":
                with st.expander(f"Ver execução de {exercicio}"):
                    st.video(link_video[0])

        st.divider()
        
        # --- LÓGICA ATUALIZADA: BARRA DE PROGRESSO E HISTÓRICO ---
        if total_exercicios > 0:
            porcentagem = progresso_atual / total_exercicios
            st.progress(porcentagem, text=f"Progresso: {progresso_atual} de {total_exercicios} concluídos")
            
            if progresso_atual == total_exercicios:
                st.success("🎉 Parabéns! Você concluiu todo o treino de hoje.")
                
                df_hist = carregar_historico()
                hoje = date.today().strftime("%d/%m/%Y")
                
                # Verifica se o treino de hoje já foi salvo para não duplicar se você recarregar a página
                ja_treinou = not df_hist[(df_hist["Data"] == hoje) & (df_hist["Treino Concluído"] == dia_hoje)].empty
                
                if not ja_treinou:
                    if st.button("💾 Salvar Treino no Histórico", use_container_width=True):
                        novo_historico = pd.DataFrame({"Data": [hoje], "Treino Concluído": [dia_hoje]})
                        df_hist = pd.concat([df_hist, novo_historico], ignore_index=True)
                        salvar_historico(df_hist)
                        st.rerun()
                else:
                    st.info("✅ O treino de hoje já está registrado no seu histórico!")