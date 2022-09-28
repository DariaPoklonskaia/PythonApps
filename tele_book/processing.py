def search_option(to_find):
    with open('book.csv', 'r') as file:
        for line in file: 
            if to_find in line:
                with open('output.csv', 'a') as file:
                    file.write(line + '\n')
                    print(line, end='\n') 


# test = 'ася'
# print(search_option(test))