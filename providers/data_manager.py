import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Inicia a conexão com o Google Sheets usando as credenciais da nuvem
conn = st.connection("gsheets", type=GSheetsConnection)

# Substitua por a sua URL real da planilha do Google!
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/1Lbpv0sOIkUYgpIL4oMhgSpcbLzXRv9Mdra3SQPfQHsY/edit?usp=sharing"

# --- DADOS DOS EXERCÍCIOS ---
def carregar_treino():
    try:
        # Lê a aba "Treino" da planilha
        df = conn.read(spreadsheet=URL_PLANILHA, worksheet="Treino")
        return df.dropna(how="all") # Remove linhas totalmente vazias
    except Exception:
        return pd.DataFrame(columns=["Exercício", "Séries", "Repetições", "Link do Vídeo"])

def salvar_treino(df):
    conn.update(spreadsheet=URL_PLANILHA, worksheet="Treino", data=df)

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