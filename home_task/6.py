def function1():
    function2()

def function2():
    function3()

def function3():
    class MyException(Exception):
        pass
    raise MyException("My error")
function1()

