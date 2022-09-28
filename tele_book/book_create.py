
import data_generation as dg
import processing as pr


def create_book(N):
    for i in range(0, N + 1):
        column1 = dg.data_gather()[0]
        column2 = dg.data_gather()[1]
        column3 = str(dg.data_gather()[2])
        with open('book.csv', 'a') as file:
            file.write('{}; {}; {}\n'
                    .format(column1, column2, column3))






