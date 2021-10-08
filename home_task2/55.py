def swap(function):
    def wrapper(*args, **kwargs):
        function(*args[::-1], **kwargs)
    return wrapper
@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)

