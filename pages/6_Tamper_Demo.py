# pages/6_Tamper_Demo.py
import streamlit as st

st.title("🛠️ Tamper Demo (Manual Edit)")

network = st.session_state.get("network", None)
if not network:
    st.warning("⚠️ Please go to '1. Node Setup' first.")
    st.stop()

# Select node
roll = st.selectbox("Select Node to Tamper", list(network.nodes.keys()))
node = network.nodes[roll]["blockchain"]

# Select block (excluding genesis block at index 0)
block_indices = [b.index for b in node.chain if b.index > 0]
if not block_indices:
    st.warning("⚠️ No blocks available to tamper (only Genesis block exists).")
    st.stop()

block_index = st.selectbox("Select Block Index", block_indices)

# Get the block
block_to_tamper = node.chain[block_index]

st.subheader("🔍 Current Block Data")
st.json({
    "Index": block_to_tamper.index,
    "Transaction": block_to_tamper.transaction,
    "Hash": block_to_tamper.hash,
    "Previous Hash": block_to_tamper.previous_hash
})

# Input new tampered amount
new_amount = st.number_input("Enter new amount to overwrite transaction:", min_value=1.0, step=1.0)

if st.button("✏️ Tamper Block"):
    block_to_tamper.transaction["amount"] = new_amount
    # Important: We do NOT recalc hash → chain becomes invalid
    st.error(f"Block {block_index} in {roll}'s blockchain tampered! Amount changed to {new_amount}.")

# Show validation after tampering
st.subheader("✅ Validation Results After Tampering")
results = network.validate_all()
for r, is_valid in results.items():
    st.write(f"Node {r}: {'✅ Valid' if is_valid else '❌ Invalid'}")