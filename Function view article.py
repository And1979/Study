def view_notes(login):
    '''The function of viewing notes with a preview of 5 words and further selection of actions with the note.
     We also need to add 2 functions for editing and deleting.
     For the test, instead of calling functions, I added a print.
    Функция просмотра заметок с предварительным просмотром из 5 слов и дальнейшего выбора действий с заметкой.
     Еще нужно добавить 2 функции для редактирования и удаления.
     Для теста вместо вызова функций добавил принт.
    '''
    print ('\n' + 'Веберите номер для чтения!' + '\n' + '\n' + 'Ваши заметки:')
    with open(login + '.txt', 'r') as file:
        notes = file.read().split(';')[::-1]
        for note in range(len(notes)):
            print(str(note + 1) + ' ' + ' '.join(notes[note].split()[:5]))
        number_selection = input()
        if number_selection.isdigit():
            if int(number_selection) - 1 < len(notes):
                print(notes[int(number_selection) - 1])
                print('\n' + 'Ваши варианты (веберите один):' + '\n' + 'Редактировать ' + '\n' + 'Удалить' + '\n' +
                      'Закрыть (вернуться к выбору заметки)' + '\n' + 'Выйти (в главное меню)')
            else:
                print('Такого номера заметки нет, попробуйте еще раз внимательно!')
                view_notes(login)
        else:
            print('\n' + 'Вы ввели не номер заметки, повторите ещё раз внимательно!')
            view_notes(login)
        choice_of_action = input()
        while choice_of_action == str(choice_of_action):
            if choice_of_action == 'Редактировать':
                print('ред')
                break
                #edit_note(login, number_selection)
            elif choice_of_action == 'Удалить':
                print('уд')
                break
                #delete_note(login, number_selection)
            elif choice_of_action == 'Закрыть':
                view_notes(login)
            elif choice_of_action == 'Выйти':
                print('вых')
                break
                #main_menu(login)
            else:
                print('\n' + 'Такого варианта нет, будьте внимательны!!!!')
                print('\n' + 'Ваши варианты (веберите один):' + '\n' + 'Редактировать ' + '\n' + 'Удалить' + '\n' +
                        'Закрыть (вернуться к выбору заметки)' + '\n' + 'Выйти (в главное меню)')
                choice_of_action = input()


view_notes('qwerty')


'''
help(view_notes)
или
print(view_notes.__doc__)
Вызов описания функции
'''
