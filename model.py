# Нет принтов и инпутов
import json

phone_book = {}
phone_book_copy = {}
path = '/phones.json'

def open_file():
    global phone_book, phone_book_copy

    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_book = json.load(file)
            phone_book_copy = phone_book.copy()
        return True
    except:
        return False

def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
        return True
    except:
        return False

def check_id():
    if phone_book:
        return max(list(map(int,phone_book))) + 1
    return 1

def new_contact(new: {int: dict[str, str]}):
    contact = {check_id(): new}
    phone_book.update(contact)

def search(word: str) -> dict[int:dict[str,str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result

def delete_contact(index: str):
    try:
        del_cnt = phone_book.pop(str(index))
        return del_cnt
    except:
        return False

def change_contact(contact: str, data_cnt:dict[str, str]):
    phone_book[contact].update(data_cnt)

def save_check():
    return False if phone_book == phone_book_copy else True



