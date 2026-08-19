def validatePostalCode(code):
    valid = False
    if len(code)==7:
        if code[0].isalpha() and code[1].isdecimal() and code[2].isalpha() and code[3].isspace() and code[4].isdecimal() and code[5].isalpha() and code[6].isnumeric():
            valid = True
    elif len(code)==6:
        if code[0].isalpha() and code[1].isdecimal() and code[2].isalpha() and code[3].isdecimal() and code[4].isalpha() and code[5].isnumeric():
            valid = True
    else:
        valid = False
    return (valid)



postal = input ("Please enter a Canadian postal code:")

val = validatePostalCode(postal)
if val:
    print("You have entered a valid postal code!")
else:
    print("Please try again!")

        
