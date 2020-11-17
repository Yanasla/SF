def print_config(**kwargs):  
    for key, value in kwargs.items():  
        print(key, ": ", value)  
  
  
print_config(school="skillfactory")  
# => school :  skillfactory  
print_config(school="skillfactory", course="analytics", language="python")  
# => school :  skillfactory  
# course :  analytics  
# language :  python  