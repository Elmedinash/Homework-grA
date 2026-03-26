#Create a function withdraw(balance, amount) that:

# Raises an error if:
 # - amount is greater than balance
  #  - amount is negative
#- Otherwise returns the new balance

def withdraw(balance, amount):
   
    if amount > balance:
        raise ValueError("Amount is greater then balance")
    if amount <=0:
        raise ValueError("Amount can not be negative")
    return balance - amount
    
print(withdraw(300, 30))