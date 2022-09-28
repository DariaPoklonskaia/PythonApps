def search_option(to_find):
    with open('book.csv', 'r') as file:
        for line in file: 
            if to_find in line:
                return line 


# test = 'ася'
# print(search_option(test))