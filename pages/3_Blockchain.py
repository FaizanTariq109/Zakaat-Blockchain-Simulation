# pages/3_Blockchain.py
import streamlit as st

st.title("📜 Blockchain Ledger")

network = st.session_state.get("network", None)
if not network:
    st.warning("⚠️ Please go to '1. Node Setup' first.")
    st.stop()

for roll, node in network.nodes.items():
    st.subheader(f"Blockchain of {roll}")
    for block in node["blockchain"].chain:
        st.json({
            "Index": block.index,
            "Timestamp": block.timestamp,
            "Transaction": block.transaction,
            "Hash": block.hash,
            "Previous Hash": block.previous_hash
        })