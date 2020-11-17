values = [-7, -7, 7, 7]
std = 42

def count_std():
    mean = sum(values)/len(values)
    std = (sum([(value-mean)**2 for value in values])/len(values))**0.5
    return std

def normalize(value):
    result = value/std
    return result 

print(normalize(21))

#hello = 'world'  
#def change():  
    #hello = hello + 'bro'  
#print(change())  

piglet = "Naf-Naf"  
def who_is_piglet():  
    global piglet  
    piglet += '!'  
  
who_is_piglet()  
print(piglet)  
# => Naf-Naf!  

rabbits = 0

def count_rabbits(spotted):
    global rabbits
    rabbits += spotted

    
count_rabbits(3)
count_rabbits(5)
print(rabbits)

