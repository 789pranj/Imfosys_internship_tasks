def get_suspecious_transaction(transactions):
    suspecious = []
    
    for transaction in transactions:
        if(transaction["amount"] > 50000):
            suspecious.append(transaction)
            
    return suspecious

def analyse (transactions):
    suspecious = get_suspecious_transaction(transactions)
    
    map = {}
    ans = []
    
    for transaction in suspecious:
        location = transaction["location"]

        if location in map:
            map[location].append(transaction)
        else:
            map[location] = [transaction]

    for location, transaction in map.items():
        if len(transaction) > 0:     
            ans.extend(transaction)
            
    return ans        

transactions = [
    {"id": 1, "amount": 500, "location": "Chennai"},
    {"id": 2, "amount": 45000, "location": "Delhi"},
    {"id": 3, "amount": 52000, "location": "Chennai"},
    {"id": 4, "amount": 200, "location": "Coimbatore"}
]


result = analyse(transactions=transactions)

print(result)