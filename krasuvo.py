from functools import wraps


class StringWrapper:
    def __init__(self, start='', end=''):
        self.start = start
        self.end = end

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return str(func(*args, **kwargs)).join([self.start, self.end])
        return wrapper


make_bold = StringWrapper('<b>', '</b>')
make_italic = StringWrapper('<i>', '</i>')


@make_bold
def make_krasuvo(text: str):
    return ' '.join(
        (char.upper() for char in text)
    )

# print(make_krasuvo.__name__)
