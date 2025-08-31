# pages/2_Transactions.py
import streamlit as st

st.title("💸 Transactions")

network = st.session_state.get("network", None)
if not network:
    st.warning("⚠️ Please go to '1. Node Setup' first to initialize the blockchain network.")
    st.stop()

sender = st.selectbox("Select Sender", list(network.nodes.keys()))
receiver = st.selectbox("Select Receiver", list(network.nodes.keys()))
amount = st.number_input("Enter Amount", min_value=1.0, step=1.0)

if st.button("Send Transaction"):
    result = network.make_transaction(sender, receiver, amount)
    st.info(result)