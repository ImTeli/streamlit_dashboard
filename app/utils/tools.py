from time import sleep
import streamlit as st


def convert_csv(df):
    return df.to_csv(index=False).encode("utf-8")


def success_msg():
    success = st.success("Arquivo baixado com sucesso!", icon="✔️")
    sleep(3)
    success.empty()
