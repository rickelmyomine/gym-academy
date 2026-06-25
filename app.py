import streamlit as st
from ui.treino_page import mostrar_pagina_treino
from ui.cronograma_page import mostrar_pagina_cronograma
from ui.modo_treino_page import mostrar_pagina_modo_treino
from ui.historico_page import mostrar_pagina_historico

# 1. Alterar o nome da App no separador do navegador e manter centrado
st.set_page_config(page_title="Gym Academy", page_icon="logo.png", layout="centered")

# Ocultar o menu padrão e o rodapé do Streamlit para parecer mais com uma app de telemóvel
esconder_estilo_padrao = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(esconder_estilo_padrao, unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---

# 2. Adicionar o logótipo no topo do menu lateral
# O comando abaixo tenta carregar a imagem 'logo.png'. 
# Se o seu logótipo tiver outro nome, altere no texto abaixo.
try:
    st.sidebar.image("logo.png", use_container_width=True)
except:
    # Caso não encontre a imagem, não dá erro, apenas exibe o texto
    st.sidebar.title("Gym Academy")

st.sidebar.markdown("---") # Linha para separar o logo do menu

menu = st.sidebar.radio(
    "Navegação:", 
    ["💪 Modo Treino", "🏆 Histórico", "📅 Cronograma da Semana", "🏋️ Área de Treino"]
)

# --- ROTEAMENTO DE PÁGINAS ---
if menu == "💪 Modo Treino":
    mostrar_pagina_modo_treino()
elif menu == "🏆 Histórico":
    mostrar_pagina_historico()
elif menu == "📅 Cronograma da Semana":
    mostrar_pagina_cronograma()
elif menu == "🏋️ Área de Treino":
    mostrar_pagina_treino()