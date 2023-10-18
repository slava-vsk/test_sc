print(" !!! Нова версія застосунку Калькулятор !!!")
def dod_arg (a, b): 
    try:
        assert a == "","некоректні аргументи"
    except AssertionError as e:
        print(str(e))
        try:
            assert b == "","некоректні аргументи"
        except AssertionError as e:
            print(str(e))
            return a + b

def vid_arg (a, b): 
    try:
        assert a == "","некоректні аргументи"
    except AssertionError as e:
        try:
            assert b == "","некоректні аргументи"
        except AssertionError as e:
            return a - b

def mnz_arg (a, b): 
    try:
        assert a == "","некоректні аргументи"
    except AssertionError as e:
        try:
            assert b == "","некоректні аргументи"
        except AssertionError as e:
            return a * b

def dil_arg (a, b):
    try:
        assert a == "","некоректні аргументи"
    except AssertionError as e:
        try:
            assert b == "","некоректні аргументи"
        except AssertionError as e:
            assert b == 0, "Ділення на нуль !!!"
            return a / b if b !=0 else "Ділення на нуль !!!"

# test our function
print(dod_arg(5,6))
print(dod_arg("",6))
print(dod_arg(5,""))

assert vid_arg(2,5) == -7,"Увага! Помилка."
