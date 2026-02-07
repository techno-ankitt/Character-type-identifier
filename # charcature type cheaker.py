# character type checker
char = input("Enter your symbol: ")

if len(char) == 1:
    if 'A' <= char <= 'Z':
        print("Entered char is in Uppercase")
        
    elif 'a' <= char <= 'z':
        print("Entered char is in Lowercase")
        
    elif '0' <= char <= '9':
        print("Entered char is a Number")
        
    else:
        print("Entered char is a Special Character (like @, #, $, %)")
        
else:
    print("Invalid input! Please enter only a single character.")
