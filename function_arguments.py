def printme(str): #required type argument
    print(str)
    return
printme('pankaj')
#####################################################
def print_name_age(name,age): #keyword typeargument
    print('Name:',name)
    print("Age:",age)
print_name_age(name="pankaj verma",age="23")
print_name_age(name="shubham verma",age="20")
#######################################################
def print_lenth(arg,*var): #variable_length function argument
    print(arg)
    for v in var:
        print(v)
print_lenth(10,20,30)