#Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.
# Примерная функциональность для реализации:
# получить список всех людей
# CRUD (create-read-update-delete) для определенного человека в БД
# импортировать / экспортировать людей в БД

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Поиск")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


