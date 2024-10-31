


def input_error(func):
    def handler(*args):
        try:
            return func(*args)
        except (ValueError):
            return'Please give me: name phone_number'
        except KeyError:
            return 'There is no such contact in database!'
        except IndexError:
            return 'Please give me name!'
    return handler


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        return 'There is already such contact, try command: change'
    else:
        contacts[name] = phone
        return f'Contact added'

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        old_phone = contacts[name]
        contacts[name] = phone
        return f'Old contact: {name} {old_phone}. Updated to: {phone}'
    else:
        return 'There is no such contact, try command: add'


@input_error
def phone_number(args, contacts):
    name = args[0]
    if name in contacts:
        phone = contacts.get(name)
        return f'Phone number of {name} is {phone}'
    else:
        raise KeyError
    
    
def all_numbers(contacts):
    if len(contacts)>0:
        return contacts
    else:
        return 'There is no any contacts!'
#EOF