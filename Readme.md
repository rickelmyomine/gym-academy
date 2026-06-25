# 🏋️ Gym Academy

**Gym Academy** é um aplicativo web pessoal desenvolvido em Python com [Streamlit](https://streamlit.io/) para auxiliar no planejamento, execução e registro de rotinas de treino na academia.

## ✨ Funcionalidades

O aplicativo foi dividido em quatro módulos principais para facilitar o uso no dia a dia pelo celular:

* **💪 Modo Treino:** O "checklist" da academia. Seleciona o treino do dia, exibe os exercícios, possui atalhos embutidos para os vídeos de execução e uma barra de progresso para acompanhar a sessão.
* **🏆 Histórico:** Salva automaticamente a data e o treino concluído (quando a barra de progresso atinge 100%) para você acompanhar a sua consistência.
* **📅 Cronograma da Semana:** Permite organizar os exercícios cadastrados e atrelá-los a dias específicos da semana.
* **🏋️ Área de Treino:** O "banco de dados" pessoal. Permite cadastrar novos exercícios, definir séries e repetições, anexar links de vídeos (YouTube) e remover exercícios antigos.

## 📁 Arquitetura do Projeto

O código foi modularizado para facilitar a manutenção e separar as responsabilidades de dados e interface:

```text
GYM-ACADEMY/
│
├── .streamlit/
│   └── config.toml           # Tema visual do app (Dark Mode + Verde Neon)
│
├── providers/
│   └── data_manager.py       # Gerenciador de dados (Leitura/Escrita dos CSVs via Pandas)
│
├── ui/
│   ├── cronograma_page.py    # Tela de montagem da semana
│   ├── historico_page.py     # Tela de acompanhamento de consistência
│   ├── modo_treino_page.py   # Tela de execução do treino diário
│   └── treino_page.py        # Tela de cadastro de exercícios
│
├── app.py                    # Maestro principal (Roteamento e Menu Lateral)
├── requirements.txt          # Dependências do projeto (streamlit, pandas)
├── logo.png                  # Identidade visual do app
│
└── *.csv                     # Arquivos locais gerados automaticamente pelo Pandas

🚀 Como executar localmente

Certifique-se de ter o Python instalado.

Clone este repositório.

Instale as dependências executando o comando:

pip install -r requirements.txt


Inicie o aplicativo com o comando:

python -m streamlit run app.py


☁️ Hospedagem

Este projeto está configurado para ser hospedado gratuitamente no Streamlit Community Cloud. Basta conectar o repositório do GitHub à plataforma e definir o app.py como o arquivo principal.


---

Com o logo na pasta, o `requirements.txt` alinhado e o `README.md` pronto, o nosso projeto em código está 100% concluído! 

Podemos agora retomar aquele passo a passo de subir os arquivos para o GitHub e publicar o