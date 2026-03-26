#Write a function that:
# Takes a list of strings: ["10", "20", "abc", "40"]
#Converts valid values to integers
#  Ignores invalid values without crashing
values = ["10", "20", "abc", "40"]

def clean_data(values):
    cleaned_values = []

    for value in values:
        try:
            cleaned_values.append(int(value))
        except:
            continue
    return cleaned_values
cleaned_values = clean_data(values)
print(cleaned_values)