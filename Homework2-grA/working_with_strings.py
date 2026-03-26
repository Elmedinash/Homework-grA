text = "Data engineering is powerful and data pipelines are important"

#  Write code to:

#- Count how many times the word "data" appears (case insensitive)
#- Replace "data" with "DATA"

def check_text(text):

    count = text.lower().count("data")

    new_text = text.lower().replace("data", "DATA")

    return count, new_text

count, updated_text = check_text(text)
print("Count:", count)
print("Updated text:", updated_text)
