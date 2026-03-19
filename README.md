# Criminal Evidence Management System Using Blockchain

A secure web-based criminal evidence management system built with Django and Ethereum blockchain to ensure tamper-proof storage and retrieval of criminal evidence records.

## 🔗 Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python 3.8, Django 2.1.7
- **Blockchain**: Ethereum (Solidity 0.8.11), Web3.py, Ganache
- **Database**: SQLite3

## 📌 Features

- Tamper-proof evidence storage on Ethereum blockchain
- Role-based access for Admin and Police Officers
- Add, view and access crime evidence records
- Evidence image upload with blockchain transaction receipts
- Smart contract-based user and evidence management

## 🖥️ Screenshots

> Admin Login → Add Officers → Add Evidence → View Evidence

## ⚙️ Prerequisites

- Python 3.8
- Node.js & npm
- Ganache CLI

## 🚀 Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/criminal-evidence-blockchain.git
cd criminal-evidence-blockchain
```

### 2. Create and activate virtual environment
```bash
cd C:\Users\<your-username>\Desktop
py -3.8 -m venv django_venv
django_venv\Scripts\activate.bat
cd criminal-evidence-blockchain
```

### 3. Install dependencies
```bash
pip install numpy==1.21.6
pip install Django==2.1.7
pip install Pillow==9.5.0
pip install web3==4.7.2
pip install urllib3==1.26.19
pip install requests==2.28.1
pip install rsa==4.9
pip install py-solc-x
```

### 4. Start Ganache (open a new terminal)
```bash
npm install -g ganache-cli
ganache-cli -p 9545
```

### 5. Deploy Smart Contract
```bash
python deploy_contract.py
```
> Copy the deployed contract address from the output and update `deployed_contract_address` in `EvidenceApp/views.py`

### 6. Run migrations
```bash
python manage.py migrate
```

### 7. Start the server
```bash
python manage.py runserver
```

### 8. Open browser
```
http://127.0.0.1:8000/index.html
```

## 🔐 Login Credentials

| Role   | Username | Password |
|--------|----------|----------|
| Admin  | admin    | admin    |
| Officer | (created by admin) | (set by admin) |

## 📁 Project Structure

```
├── Evidence/               # Django project settings
├── EvidenceApp/            # Main application
│   ├── templates/          # HTML templates
│   ├── static/             # CSS and images
│   ├── views.py            # Application logic
│   └── urls.py             # URL routing
├── Evidence.sol            # Solidity smart contract
├── Evidence.json           # Contract ABI
├── deploy_contract.py      # Contract deployment script
└── manage.py               # Django management
```

## 📝 Note

> Every time Ganache is restarted, you must redeploy the smart contract using `python deploy_contract.py` and update the contract address in `EvidenceApp/views.py`.

## 👨‍💻 Author

- **Your Name** - [GitHub](https://github.com/<your-username>)

## 📄 License

This project is for educational purposes only.
