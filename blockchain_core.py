import hashlib
import time

class Block:
    def __init__(self, index, transaction, previous_hash, roll_number):
        self.index = index
        self.timestamp = time.time()
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.roll_number = roll_number
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.index}{self.timestamp}{self.transaction}{self.previous_hash}{self.roll_number}"
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self, roll_number):
        self.chain = []
        self.roll_number = roll_number
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, {"sender": "None", "receiver": self.roll_number, "amount": 200}, "0", self.roll_number)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transaction):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), transaction, latest_block.hash, self.roll_number)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True

class BlockchainNetwork:
    def __init__(self):
        self.nodes = {}
        self.zakat_pool = 0

    def add_node(self, roll_number):
        if roll_number not in self.nodes:
            self.nodes[roll_number] = {
                "blockchain": Blockchain(roll_number),
                "balance": 200
            }

    def make_transaction(self, sender, receiver, amount):
        if sender not in self.nodes or receiver not in self.nodes:
            return "Invalid sender/receiver!"

        if self.nodes[sender]["balance"] < amount:
            return "Insufficient balance!"

        zakat = round(amount * 0.025, 2)
        send_amount = amount - zakat

        # Update balances
        self.nodes[sender]["balance"] -= amount
        self.nodes[receiver]["balance"] += send_amount
        self.zakat_pool += zakat

        # Record transaction
        tx = {"sender": sender, "receiver": receiver, "amount": amount, "zakat": zakat}
        self.nodes[sender]["blockchain"].add_block(tx)
        self.nodes[receiver]["blockchain"].add_block(tx)

        return f"✅ Transaction successful! {amount} sent from {sender} to {receiver}. Zakat {zakat} added."

    def validate_all(self):
        results = {}
        for roll, node in self.nodes.items():
            results[roll] = node["blockchain"].is_chain_valid()
        return results