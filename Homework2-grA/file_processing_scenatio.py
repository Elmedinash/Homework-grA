#Write a script that:

#- Reads a file
#- Counts:
# - total lines
#  - empty lines
#- Handles error if file does not exist



def analyze_file(filename):

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            total_lines = len(lines)
            empty_lines = sum(1 for line in lines if line.strip() == " ")

            print(f"Total number of lines: {total_lines}")
            print(f"Total numer of empty lines: {empty_lines}")
    
    except FileNotFoundError:
        print("File not found")

analyze_file("example.txt")