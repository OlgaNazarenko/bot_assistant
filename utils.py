from functools import wraps

def input_error(handler):
    @wraps(handler)
    def wrapper(*args, **kwargs):
        try:
            result = handler(*args, **kwargs)
        except KeyError as e:
            print(f'You entered a wrong name {e} that is not in the list. Please enter once again')
        except ValueError as e:
            print(e)
        except IndexError as e:
            print('You entered a wrong data. Please enter once again')
        else:
            return result

    return wrapper


def check_phone(phone: str) -> str:
    pattern = r"(^380|0|80)\d{9}$"
    match = re.fullmatch(pattern, phone)
    if not match:
        raise ValueError("Invalid, please enter a valid phone number")

    return phone