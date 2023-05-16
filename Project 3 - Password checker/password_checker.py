password = input("Please enter your password: ")
special_chars = "!,@,%,$,#"

def contains_special_char(password):
    for char in special_chars.split(","):
        if char in password:
            return True
    return False

if password == "":
   print("Error: Please do not leave the password blank.")
else:
    if not password.isupper() and not password.islower() and len(password) >= 8 and contains_special_char(password):
        print("Success: Your password is strong and secure.")
    else: 
        print("Error: Your password must contain at least one uppercase character, one lowercase character, and one special character. It must also be at least 8 characters long.")