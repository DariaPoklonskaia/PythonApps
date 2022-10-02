
fields = ["id", "last_name", "first_name", "position", "phone_number", "salary"]


def perform_search():
    to_find = input('Type what you what to find: ')
    with open('employees.csv', 'r') as file:
        for line in file: 
            if to_find in line:
                string = line.replace(';', ' ')
                print(string, end='\n')




def select_by_position():
    positions=[]
    with open('employees.csv', 'r') as file:
        for line in file:
            lst=[]
            lst = line.split(';')
            if lst[3] not in positions:
                positions.append(lst[3])
    positions_enu = list(enumerate(positions))
    print(positions_enu)

    select = int(input('type position number to select: '))
    select = str(positions[select])
    with open('employees.csv', 'r') as file:
        for line in file: 
            if select in line:
                string = line.replace(';', ' ')
                print(string, end='\n')
 
 


def select_by_salary():
    salaries=[]
    with open('employees.csv', 'r') as file:
        for line in file:
            lst=[]
            lst = line.split(';')
            salaries.append(lst[5])
    salaries.pop(0)
    salaries = list(map(lambda x: int(x.replace('\n', '')), salaries))

    maxS = max(salaries)
    minS = min(salaries)
    lower_value = int(input('min salary is {}. Max salary is {}. Type lower value for range: '.format(minS, maxS)))
    upper_value = int(input('Type upper value for range: '))
    for i in range(0, len(salaries)):
        if salaries[i] <= upper_value and salaries[i] >= lower_value:
            with open('employees.csv', 'r') as file:
                for j, line in enumerate(file): 
                    if i + 1 == j:
                        stringg = line.replace(';', ' ')
                        print(stringg, end='\n')
                        
                    


   
