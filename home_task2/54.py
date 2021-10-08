def decorator(function):
    def wrapper(lst):
        count = function(lst)
        if count ==  0:
            print('Нет(')
        elif count > 10:
            print('Очень много')
    return wrapper
@decorator
def s(lst):
    count = 0
    for x in lst:
        if x%2 == 0:
            count +=1
    return count
s([3, 5])
