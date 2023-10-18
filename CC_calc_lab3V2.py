print(" !!! Нова версія застосунку Калькулятор !!!")
def dod_arg (a, b): 
    try:
        assert a == "","некоректні аргументи"
    except AssertionError as e:
        try:
            assert b == "","некоректні аргументи"
        except AssertionError as e:
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
            return a / b

# test our function
      
dod_arg(5,6)   
dod_arg("",6)   
dod_arg(5,"")   

vid_arg(2,5)
vid_arg(10,5)
vid_arg("",5)
vid_arg(2,"")

mnz_arg(7,4)
mnz_arg(7,0)
mnz_arg("",4)
mnz_arg(7,"")

dil_arg(3,7)
dil_arg(7,3)
dil_arg(3,0)
dil_arg(0,7)
dil_arg(3,"")
dil_arg("",7)

