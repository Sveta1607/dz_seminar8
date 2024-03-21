from import_data import import_data
from find_number import find_number
from add_phone_number import add_phone_number
from change_phone_number import change_phone_number
from delete_contact import delete_contact
from show_phonebook import show_phonebook
from read_file_to_dict import read_file_to_dict


def choose_action(phonebook):
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            add_phone_number(phonebook)
        elif user_choice == '4':
           change_phone_number(phonebook)
        elif user_choice == '5':
            delete_contact(phonebook)
        elif user_choice == '6':
            show_phonebook(phonebook)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue