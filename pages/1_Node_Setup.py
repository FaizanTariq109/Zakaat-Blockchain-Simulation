# pages/1_Node_Setup.py
import streamlit as st
from blockchain_core import BlockchainNetwork

st.title("🧑‍🎓 Node Setup")

# Initialize network in session_state
if "network" not in st.session_state:
    st.session_state["network"] = BlockchainNetwork()

network = st.session_state["network"]

roll_number = st.text_input("Enter your Roll Number:")
if st.button("Add Node"):
    if roll_number:
        network.add_node(roll_number)
        st.success(f"Node with Roll Number {roll_number} added successfully!")
    else:
        st.warning("Please enter a valid roll number.")

st.subheader("📋 Existing Nodes")
for roll in network.nodes.keys():
    st.write(f"- {roll}")