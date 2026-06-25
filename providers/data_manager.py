import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Inicia a conexão
conn = st.connection("gsheets", type=GSheetsConnection)

# Substitua pela sua URL real da planilha
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/1Lbpv0sOIkUYgpIL4oMhgSpcbLzXRv9Mdra3SQPfQHsY/edit?usp=sharing"

# --- DADOS DOS EXERCÍCIOS ---
def carregar_treino():
    try:
        # Tenta ler a planilha
        df = conn.read(spreadsheet=URL_PLANILHA, worksheet="Treino", ttl=0)
        return df.dropna(how="all")
    except Exception as e:
        # Se der erro, mostra na tela vermelha o motivo (ajuda a identificar o 401)
        st.error(f"Erro ao tentar ler a aba Treino: {e}")
        return pd.DataFrame(columns=["Exercício", "Séries", "Repetições", "Link do Vídeo"])

def salvar_treino(df):
    try:
        conn.update(spreadsheet=URL_PLANILHA, worksheet="Treino", data=df)
    except Exception as e:
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