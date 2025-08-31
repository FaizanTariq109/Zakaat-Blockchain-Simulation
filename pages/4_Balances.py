# pages/4_Balances.py
import streamlit as st
import pandas as pd

st.title("💰 Balances & Zakat Pool")

network = st.session_state.get("network", None)
if not network:
    st.warning("⚠️ Please go to '1. Node Setup' first.")
    st.stop()

balances = [{"Roll Number": roll, "Balance": node["balance"]} for roll, node in network.nodes.items()]
df = pd.DataFrame(balances)

st.table(df)
st.success(f"📦 Zakat Pool Balance: {network.zakat_pool}")