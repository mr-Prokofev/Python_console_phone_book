main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать все контакты',
             'Добавить контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

select_menu = 'Выберите пункт меню: '
input_error = f'Ошибка ввода. Введите число от 1 до {len(main_menu)-1}'
new_contact = {'name': 'Введите имя контакта: ',
               'phone': 'Введите телефон: ',
               'comment': 'Введите комментарий: '}
empty_book = 'Телефонная книга пуста или не открыта'
load_successfull = 'Телефонная книга успешно загружена'
save_successfull = 'Телефонная книга успешно сохранена'
load_error = 'Ошибка. Телефонная книга не загружена'
save_error = 'Ошибка. Телефонная книга не сохранена'

search_word = 'Введите искомое значение: '
error_delete = 'Ошибка. Проверьте параметры!'
data_is_different = 'Внесены изменения в исходный файл. Сохранить? y - да'
not_save = 'Телефонная книга не сохранена!'
def empty_search(word: str) -> str:
    return f'По слову {word} ничего не удалось найти'
def add_successfull(name: str) ->str:
    return f'Контакт {name} добавлен!'

exit_message = 'Работа завершена!'
id_question = "Введите ID контакта: "

def contact_complete_delete(name: str) -> str:
    return f'Контакт {name} удален!'

def change_successfull(name: str, new_name: str) -> str:
    return f'Контакт {name} успешно изменен на {new_name}'

