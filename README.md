# 📦 Mini Blockchain with Zakat System  

A **mini blockchain system** built using **Python** and **Streamlit** for academic purposes.  
The system simulates transactions between student nodes, automatically deducts **2.5% zakat**, and maintains a secure blockchain ledger.  
It also includes **block validation** and a **tamper demo** to demonstrate immutability.  

---

## 🚀 Features  

- 🧑‍🎓 **Node Creation**  
  - Add students by their **roll numbers**.  
  - Each new node starts with **200 default coins**.  

- 💸 **Transactions**  
  - Send coins from one student to another using their roll number.  
  - **2.5% zakat** automatically deducted from each transaction and added to a global zakat pool.  

- ⛓️ **Blockchain Ledger**  
  - Each block contains:  
    - Transactions  
    - Timestamp  
    - Hash & Previous Hash  
    - Roll number seed key  
  - View all blocks with details.  

- 📊 **Balances Dashboard**  
  - See balances of all students in a table.  
  - Visualize distribution with charts.  
  - Track zakat pool growth.  

- 🔐 **Validation**  
  - Verify integrity of the blockchain.  
  - Detect tampering in any block.  

- 🛠️ **Tamper Demo**  
  - Manually change transaction amounts in a block.  
  - Revalidate to see how blockchain immutability works.  

---

- ## Install Dependencies
   - pip install streamlit pandas


- ## Run the App
   - streamlit run Home.py

 ## 📖 Learning Objectives  
- 🔗 **Understand blockchain fundamentals** (blocks, hashes, immutability).  
- 💰 **Implement a simple ledger system** in Python.  
- 🕌 **Explore real-world concepts like zakat deduction**.  
- 📊 **Visualize data with Streamlit dashboards**.  
- 🛡️ **Demonstrate blockchain immutability via tampering**.  
