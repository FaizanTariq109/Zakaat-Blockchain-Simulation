import streamlit as st

st.set_page_config(page_title="Zakat Blockchain Simulation", layout="wide")

st.title("🕌 Zakat Blockchain Simulation")
st.write("""
Welcome to the **Zakat Blockchain Simulation**.  
This project demonstrates how Zakat (2.5%) is deducted from every transaction 
and securely recorded on a blockchain.

### Features
- Add student nodes (each starts with 200 coins)
- Send transactions between students (2.5% Zakat deducted automatically)
- View blockchain ledger with transactions
- Validate blockchain integrity
- Try tampering with blocks to see immutability in action
""")