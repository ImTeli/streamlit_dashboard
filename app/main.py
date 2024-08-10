import streamlit as st
from utils.data_import import df
from utils.format_number import format_number as fn
import utils.charts as chart


st.set_page_config(layout="wide", page_title="")
st.title("Dashboard de Vendas :shopping_trolley:")

aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedores"])

with aba1:
    st.dataframe(df)

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric("Receita Total", fn(df["Preço"].sum(), prefix="R$"))
        st.plotly_chart(chart.grafico_map_estado, use_container_width=True)
        st.plotly_chart(chart.grafico_rec_estado, use_container_width=True)
    with coluna2:
        st.metric("Quantidade de vendas", fn(df.shape[0]))
        st.plotly_chart(chart.grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(chart.grafico_rec_categoria, use_container_width=True)

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(chart.grafico_rec_vendedores)
