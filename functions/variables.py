#def build_piglet():  
    #piglet = 'Naf-naf'  
  
#print(piglet)  
# => NameError: name 'piglet' is not defined   

#Упс! Переменная, определённая в функции, недоступна вне её.

piglet = "Naf-Naf"  
def who_is_piglet():  
    print(piglet)  
  
print(who_is_piglet())
# => Naf-Naf   

std = 42 
def normalize(value):
    result = value/std
    return result 
    
print(normalize(21)) 

def who_in_house():  
    piglet = "Naf-Naf"  
    print(piglet)  
  
piglet = "Spy Wolf"  
who_in_house() # => Naf-Naf  
print(piglet) # => Spy Wolf  

def who_in_wood_house():  
    piglet = "Nif-Nif"  
    print(piglet)  
  
def who_in_brick_house():  
    piglet = "Naf-Naf"  
    print(piglet)  
  
print(who_in_wood_house())# => "Nif-Nif"  
print(who_in_brick_house()) # => "Naf-Naf" 
