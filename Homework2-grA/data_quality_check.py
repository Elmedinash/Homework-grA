records = [

{"user_id": 1, "age": 25, "email": "[test@gmail.com](mailto:test@gmail.com)"},

{"user_id": 2, "age": -5, "email": "invalid-email"},

{"user_id": None, "age": 30, "email": "[user@mail.com](mailto:user@mail.com)"}

]

#Validate:
# user_id must not be None
# age must be positive
# email must contain "@"

#Return:
# list of invalid records
# and reason why they are invalid

def validate_user_records(records):
    invalid_records = []

    for r in records:
        issues = []
        if r["user_id"] is None:
            issues.append("user id can not ne None")
        if r["age"] <= 0:
            issues.append("age should be positive")
        if not "@" in r["email"]:
            issues.append("email should contain '@'")
        if issues:
            invalid_records.append({"user_id": r["user_id"], "errors": [issues]})
        
    return invalid_records 
print(validate_user_records(records))
