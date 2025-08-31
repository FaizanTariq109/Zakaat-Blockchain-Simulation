# pages/5_Validation.py
import streamlit as st

st.title("✅ Blockchain Validation")

network = st.session_state.get("network", None)
if not network:
    st.warning("⚠️ Please go to '1. Node Setup' first.")
    st.stop()

results = network.validate_all()
for roll, is_valid in results.items():
    st.write(f"Node {roll}: {'✅ Valid' if is_valid else '❌ Invalid'}")