import streamlit as st
from utils.data_import import generate_df
from utils.tools import convert_csv, success_msg

st.set_page_config(
    page_title="Filtro de Dataset",
    page_icon="🚀",
    layout="wide",
)
df = generate_df()
st.title("Dataset de Vendas")

with st.expander("Colunas"):
    colunas = st.multiselect("Selecione as Colunas", list(df.columns), list(df.columns))
st.sidebar.title("Filtros")
with st.sidebar.expander("Categoria do Produto"):
    categorias = st.multiselect(
        "Selecione as categorias",
        df["Categoria do Produto"].unique(),
        df["Categoria do Produto"].unique(),
    )
with st.sidebar.expander("Preço do Produto"):
    preco = st.slider("Selecione o Preço", 0, 5000, (0, 5000))
with st.sidebar.expander("Data da Compra"):
    data_compra = st.date_input(
        "Selecione a data", (df["Data da Compra"].min(), df["Data da Compra"].max())
    )

query = """
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço  <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
"""
filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.markdown(
    f"A tabela possui: :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas."
)

coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        label="Escreva o nome do arquivo e pressione enter.",
        placeholder="nome do arquivo",
    )
    nome_arquivo += ".csv"
    st.download_button(
        label="Baixar arquivo",
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime="text/csv",
        on_click=success_msg,
    )

st.dataframe(filtro_dados)
