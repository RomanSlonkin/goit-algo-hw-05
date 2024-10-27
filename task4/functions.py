


def input_error(func):
    def handler(*args):
        try:
            result = func(*args)
            return result
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
def change_contact(args, contacts: dict):
    name, phone = args
    if name in contacts.keys():
        contacts.update({name: phone})
        return f'Contact changed to: {name}: {phone}'
    else:
        raise KeyError

@input_error
def phone_number(args, contacts):
    name = args
    if name[0] in contacts.keys():
        phone = contacts.get(name[0])
        return f'Phone number of {name} is {phone}'
    else:
        raise KeyError
    
    
def all_numbers(contacts):
    if len(contacts)>0:
        return contacts
    else:
        return 'There is no any contacts!'
#EOF