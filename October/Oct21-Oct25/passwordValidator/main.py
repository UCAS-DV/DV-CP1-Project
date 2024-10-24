special_chars = ['@','#','$','%','*','&']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print("~-~-~-~-Create Password~-~-~-~-")
print("Password must have: \n- At least 8 characters \n- At least 1 number \n- At least 1 special character")
    
while True:
    has_spec_char = False
    has_num = False
    invalid_password = False
    error_string = "Sorry! Password must have: \n"
    
    password = input("Enter New Password: ")

    for char in password:
        if char in numbers:
            has_num = True
        elif char in special_chars:
            has_spec_char = True
    
    if len(password) < 8:
        error_string += "At least 8 characters \n"
        invalid_password = True
    if has_num != True:
        error_string += "At least 1 number \n"
        invalid_password = True
    if has_spec_char != True:
        error_string += "At least 1 special character"
        invalid_password = True

    if invalid_password:
        print(error_string)
        continue

    print(f'Your password has been succesfully set to {password}')
    break