special_chars = ['@','#','$','%','*','&']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print("~-~-~-~-Create Password~-~-~-~-")

while True:
    has_spec_char = False
    has_num = False
    print("Password must have: \n- At least 8 characters \n- At least 1 number \n- At least 1 special character")
    password = input("Enter New Password: ")
    
    if len(password) < 8:
        print("Sorry! Password must be at least 8 characters long")
        continue

    for char in password:
        if char in numbers:
            has_num = True
        elif char in special_chars:
            has_spec_char = True
    
    if has_num != True or has_spec_char != True:
        print("Sorry! Password must have at least 1 number and 1 special character")
        continue

    print(f'Your password has been succesfully set to {password}')
    break