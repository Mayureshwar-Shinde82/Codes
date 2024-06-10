def My_upper(name):
    
    tempstr = ""
    for char in name:
        if char>= "a" and char <= "z":
            tempstr += chr(ord(char) - 32)
            print(tempstr)
        
        else:
            tempstr+= char
            print("Hello")
        
    return tempstr

name = input(":" "") 
print(My_upper(name))           