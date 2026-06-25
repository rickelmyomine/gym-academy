import pandas as pd
import os

ARQUIVO_CSV = "meu_treino.csv"
ARQUIVO_CRONOGRAMA = "meu_cronograma.csv"

# --- DADOS DOS EXERCÍCIOS ---
def carregar_treino():
    if os.path.exists(ARQUIVO_CSV):
        return pd.read_csv(ARQUIVO_CSV)
    return pd.DataFrame(columns=["Exercício", "Séries", "Repetições", "Link do Vídeo"])

def salvar_treino(df):
    df.to_csv(ARQUIVO_CSV, index=False)

# --- DADOS DO CRONOGRAMA ---
def carregar_cronograma():
    if os.path.exists(ARQUIVO_CRONOGRAMA):
        return pd.read_csv(ARQUIVO_CRONOGRAMA)
    return pd.DataFrame(columns=["Dia da Semana", "Exercícios"])

def salvar_cronograma(df):
    df.to_csv(ARQUIVO_CRONOGRAMA, index=False)
    # --- DADOS DO HISTÓRICO ---
ARQUIVO_HISTORICO = "meu_historico.csv"

def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        return pd.read_csv(ARQUIVO_HISTORICO)
    return pd.DataFrame(columns=["Data", "Treino Concluído"])

def salvar_historico(df):
    df.to_csv(ARQUIVO_HISTORICO, index=False)