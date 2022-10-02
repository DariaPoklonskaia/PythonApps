
import UI
import processing as pr

def To_Do():
    while True:
        x = UI.show_menu()
        if x == 1:
            pr.perform_search()
        if x == 2:
            pr. select_by_position()
        if x == 3:
            pr.select_by_salary()
        if x == 4:
            print('Bye')
            break
        

To_Do()


