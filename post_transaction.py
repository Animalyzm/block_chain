import requests
import json
import datetime

def main():
    time = datetime.datetime.now().isoformat()
    
    transaction = {
        "time": time,
        "sender": "Yamada-san",
        "receiver": "Sato-san",
        "amount": 999,
        "description": "Christmas Dinner Fee",
        "signature": "signature_sample"
    }
    
    # url = "http://127.0.0.1:8010/transaction_pool/"
    url = "https://block-chain-35tt.onrender.com/transaction_pool"
    res = requests.post(url, json.dumps(transaction))
    
    print(res.json())

if __name__ == "__main__":
    main()