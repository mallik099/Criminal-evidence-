from web3 import Web3
from solcx import compile_source, install_solc
import json

# Install solidity compiler
print("Installing Solidity compiler...")
install_solc('0.8.11')

# Read the contract
with open('Evidence.sol', 'r') as file:
    contract_source_code = file.read()

# Compile contract
print("Compiling contract...")
compiled_sol = compile_source(contract_source_code, solc_version='0.8.11')
contract_interface = compiled_sol['<stdin>:Evidence']

# Connect to Ganache
print("Connecting to Ganache...")
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:9545'))
account = w3.eth.accounts[0]

print(f"Connected! Using account: {account}")

# Deploy contract
print("Deploying contract...")
Evidence = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
tx_hash = Evidence.constructor().transact({'from': account})
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

print(f"\nContract deployed successfully!")
print(f"Contract Address: {tx_receipt.contractAddress}")

# Save ABI to Evidence.json
abi_json = {
    "abi": contract_interface['abi']
}

with open('Evidence.json', 'w') as f:
    json.dump(abi_json, f, indent=2)

print(f"\nABI saved to Evidence.json")
print(f"\nNow update views.py line 18 with this address:")
print(f"deployed_contract_address = '{tx_receipt.contractAddress}'")
