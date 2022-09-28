from random import randint
import library as li

def get_surname():
    i_sname =  randint(0, len(li.surnames) - 1)
    return li.surnames[i_sname]
    

def get_name():
    i_name =  randint(0, len(li.names) - 1)
    return li.names[i_name]
    

def get_number():
    return randint(1000, 10000)
   
    
def data_gather():
    return(get_surname(), get_name(), get_number())

