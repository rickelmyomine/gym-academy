import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Inicia a conexão com o Google Sheets usando as credenciais da nuvem
conn = st.connection("gsheets", type=GSheetsConnection)

# Substitua por a sua URL real da planilha do Google!
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/1Lbpv0sOIkUYgpIL4oMhgSpcbLzXRv9Mdra3SQPfQHsY/edit?usp=sharing"

# No seu providers/data_manager.py
def carregar_treino():
    try:
        # Tenta ler a aba
        df = conn.read(spreadsheet=URL_PLANILHA, worksheet="Treino")
        
        # Se chegar aqui, imprimimos o que ele leu para você ver
        if df is None or df.empty:
            st.warning("O código leu a planilha, mas ela parece vazia.")
            return pd.DataFrame(columns=["Exercício", "Séries", "Repetições", "Link do Vídeo"])
        
        return df
        
    except Exception as e:
        # Mostra o erro detalhado na tela
        st.error(f"Erro ao ler: {e}")
        # Retorna um DataFrame vazio para não quebrar o resto do app
        return pd.DataFrame(columns=["Exercício", "Séries", "Repetições", "Link do Vídeo"])
# --- DADOS DO CRONOGRAMA ---
def carregar_cronograma():
    try:
        df = conn.read(spreadsheet=URL_PLANILHA, worksheet="Cronograma")
        return df.dropna(how="all")
    except Exception:
        return pd.DataFrame(columns=["Dia da Semana", "Exercícios"])

def salvar_cronograma(df):
    conn.update(spreadsheet=URL_PLANILHA, worksheet="Cronograma", data=df)

# --- DADOS DO HISTÓRICO ---
def carregar_historico():
    try:
        df = conn.read(spreadsheet=URL_PLANILHA, worksheet="Historico")
        return df.dropna(how="all")
    except Exception:
        return pd.DataFrame(columns=["Data", "Treino Concluído"])

def salvar_historico(df):
    conn.update(spreadsheet=URL_PLANILHA, worksheet="Historico", data=df)