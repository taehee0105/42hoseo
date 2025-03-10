print("Hello Mars")

try:
    with open(r"./mission_computer_main.log", 'r') as file:
        lines = file.readlines()
except FileNotFoundError as e:
    print("error: ", e)
    with open(r"./error_file", 'a') as error_file:
        error_file.write(str(e))
        error_file.write("\n")
else: 
    print("순차")
    for line in lines:
        print(line, end='')
        
    print("\n역순")
    for line in lines[::-1]:
        print(line, end='')