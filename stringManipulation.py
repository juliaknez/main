userInp = input("Please enter a phrase: ")

phrase = userInp.lower()
new = ""
count = 0
next = True
nums = 0 
while count<len(phrase):
    if phrase[count].isnumeric():
        nums +=1
    elif phrase[count]=="e":
        new = new + "3"
    elif phrase[count]=="i":
        new = new +"1"
    elif phrase[count]=="o":
        new = new+"0"
    elif phrase[count].isalpha() and next:
        new=new + phrase[count].upper()
        next=False
    elif phrase[count].isalpha() and next==False:
        new=new + phrase[count]
        next=True
    else:
        new=new+phrase[count]
    
    count+=1


print(new)
print(nums)
