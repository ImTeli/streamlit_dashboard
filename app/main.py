import streamlit as st
from utils.data_import import generate_df
from utils.df_class import Teliframe


st.set_page_config(layout="wide", page_title="Proposta Indecorosa", page_icon="🌛")
st.title("Dashboard de Vendas :shopping_trolley:")

df = generate_df()
mydf = Teliframe(df)

st.sidebar.title("Filtros")

filtro_vendedor = st.sidebar.multiselect("Vendedores",df["Vendedor"].unique())
if filtro_vendedor:
    df = df[df["Vendedor"].isin(filtro_vendedor)]
filtro_pagamento = st.sidebar.multiselect("Tipo de pagamento",df["Tipo de pagamento"].unique())
if filtro_pagamento:
    df = df[df["Tipo de pagamento"].isin(filtro_pagamento)]
filtro_local = st.sidebar.multiselect("Local da compra", df["Local da compra"].unique())
if filtro_local:
    df = df[df["Local da compra"].isin(filtro_local)]
filtro_quantidade_parcelas = st.sidebar.multiselect("Quantidade de parcelas", df["Quantidade de parcelas"].sort_values(ascending=True).unique())
if filtro_quantidade_parcelas:
    df = df[df["Quantidade de parcelas"].isin(filtro_quantidade_parcelas)]


mydf.update(df)

aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedores"])

with aba1:
    st.dataframe(mydf.df)

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric("Receita Total", mydf.format_number(df["Preço"].sum(), prefix="R$"))
        st.plotly_chart(mydf.map_estado_chart(), use_container_width=True)
        st.plotly_chart(mydf.rec_estado_chart(), use_container_width=True)
    with coluna2:
        st.metric("Quantidade de vendas", (df.shape[0]))
        st.plotly_chart(mydf.rec_mensal_chart(), use_container_width=True)
        st.plotly_chart(mydf.rec_categoria_chart(), use_container_width=True)

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(mydf.rec_vendedores_chart())
    with coluna2:
        st.plotly_chart(mydf.vendas_vendedores_chart())
