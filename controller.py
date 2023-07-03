import text
import view
import model

def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successfull)
                else:
                    view.print_message(text.load_error)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successfull)
                else:
                    view.print_message(text.save_error)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.new_contact()
                model.new_contact(new)
                view.print_message(text.add_successfull(new.get('name')))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                id_contact = view.input_id_contact()
                old_name = model.phone_book[id_contact].get('name')
                new_contact_date = view.new_contact()
                model.change_contact(id_contact, new_contact_date)
                view.print_message(text.change_successfull(old_name, new_contact_date.get('name')))
            case 7:
                id_contact = view.input_id_contact()
                result = model.delete_contact(id_contact)
                if result:
                    view.print_message(text.contact_complete_delete(result.get('name')))
                else:
                    view.print_message(text.error_delete)
            case 8:
                if model.save_check():
                    view.print_message(text.data_is_different)
                    user_response = view.input_id_contact()
                    if user_response == 'y':
                        model.save_file()
                        view.print_message(text.save_successfull)
                    else:
                        model.phone_book = model.phone_book_copy
                        model.save_file()
                        view.print_message(text.not_save)
                view.print_message(text.exit_message)
                break;
