from functools import wraps


def make_bold(func):  # TODO: make class decorator
    @wraps(func)
    def wrapper(*args, **kwargs):
        res_str = '<b>'
        res_str += func(*args, **kwargs)
        res_str += '</b>'
        return res_str
    return wrapper


@make_bold
def make_krasuvo(text: str):
    return ' '.join(
        (char.upper() for char in list(text))
    )

# print(make_krasuvo.__name__)
