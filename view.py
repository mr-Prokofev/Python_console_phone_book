# Принты и инпуты
import text

def menu() -> int:
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    while True:
        select = input(text.select_menu)
        if select.isdigit() and 0 <int(select) <= len(text.main_menu) - 1:
            return int(select)
        print(text.input_error)

def print_message(message: str):
    print('\n' + '%' * len(message))
    print(message)
    print('%' * len(message) + '\n')

def new_contact():
    new = {}
    for key, val in text.new_contact.items():
        new[key] = input(val)
    return new

def show_contacts(book: dict[int: dict[str, str]], message):
    if book:
        max_name, max_phone, max_comment  = [], [], []
        for contact in book.values():
            max_name.append(len(contact.get('name')))
            max_phone.append(len(contact.get('phone')))
            max_comment.append(len(contact.get('comment')))
        size_name, size_phone, size_comment = max(max_name), max(max_phone), max(max_comment)
        print('\n' + '%' * (size_name + size_phone + size_comment + 7))
        for index, contact in book.items():
            print(f'{index:>3}. {contact.get("name"):<{size_name}} {contact.get("phone"):<{size_phone}} '
                  f'{contact.get("comment"):<{size_comment}}')
        print('%' * (size_name + size_phone + size_comment + 7) + '\n')
    else:
        print_message(message)

def search_word() -> str:
    return input(text.search_word)

def input_id_contact() ->str:
    return input(text.id_question)

