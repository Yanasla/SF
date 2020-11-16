ticket_db = [{'price': 400}, {'price': 200}, {'price': 150}]    
    
tickets_euro = []    

for ticket in ticket_db:    
    converted = ticket['price'] / 70    
    rounded = round(converted, 2)     
    formatted = '€' + str(rounded)    
    tickets_euro.append(formatted)    
        
print(tickets_euro)    
# => ['€5.71', '€2.86', '€2.14']    

ticket_db = [{'price': 400}, {'price': 200}, {'price': 150}]  
  
tickets_euro = []  
for ticket in ticket_db:  
    converted = ticket['price'] / 70  
    rounded = round(converted, 2)   
    formatted = '€' + str(rounded)  
    tickets_euro.append(formatted)  
      
      
guide_db = [{'price': 50}, {'price': 40}]  
  
guides_euro = []  
for guide in guide_db:  
    converted = guide['price'] / 70  
    rounded = round(converted, 2)   
    formatted = '€' + str(rounded)  
    guides_euro.append(formatted)  
      
      
snack_db = [{'price': 100}, {'price': 95}, {'price': 150}]  
  
snacks_euro = []  
for snack in snack_db:  
    converted = snack['price'] / 70  
    rounded = round(converted, 2)   
    formatted = '€' + str(rounded)  
    snacks_euro.append(formatted)  
  
print(tickets_euro, guides_euro, snacks_euro)  
# => ['€5.71', '€2.86', '€2.14'] ['€0.71', '€0.57'] ['€1.43', '€1.36', '€2.14']  


def to_euro(price):  
    exchange_rate = 70  
    rounded = round(price/exchange_rate, 2)  
    return '€' + str(rounded)  
  
def db_to_euro(db):  
    return [to_euro(item['price']) for item in db]  
  
  
ticket_db = [{'price': 400}, {'price': 200}, {'price': 150}]  
guide_db = [{'price': 50}, {'price': 40}]  
snack_db = [{'price': 100}, {'price': 95}, {'price': 150}]  
  
tickets_euro = db_to_euro(ticket_db)  
guides_euro = db_to_euro(guide_db)  
snacks_euro = db_to_euro(snack_db)  
  
print(tickets_euro, guides_euro, snacks_euro)  
# => ['€5.71', '€2.86', '€2.14'] ['€0.71', '€0.57'] ['€1.43', '€1.36', '€2.14']  