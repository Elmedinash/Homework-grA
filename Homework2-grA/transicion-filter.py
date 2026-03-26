transactions = [

{"id": 1, "amount": 120, "status": "completed"},

{"id": 2, "amount": -20, "status": "completed"},

{"id": 3, "amount": 50, "status": "failed"},

{"id": 4, "amount": 200, "status": "completed"}

]

#Write a function that:
# Returns only **valid transactions**
#Conditions:
    #amount must be positive
    #status must be "completed"

def validate_transactions(transactions):
    valid_transactions = []

    for transaction in transactions:
        if transaction["amount"] > 0 and transaction["status"] == "completed":
            valid_transactions.append(transaction)
    return(valid_transactions)
valid_transactions = validate_transactions(transactions)
print(valid_transactions)

    