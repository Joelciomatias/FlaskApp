import functools

def my_decorator(function):
    @functools.wraps(function)
    def function_that_call_function():
        print("*******Embrulhando função no decorator!*******")
        function()
        print("*******Fechado embrulho*******")
    return function_that_call_function

@my_decorator
def  my_function():
    print("Eu Sou uma Função")

print(my_function())