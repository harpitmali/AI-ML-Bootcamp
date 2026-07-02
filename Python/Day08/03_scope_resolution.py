# variable scope = where a variable is visiable and accessible
# scope resolution= (LEGB)  Local -> Enclosed -> Global -> Built-in

# Local
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()



# Enclosed
def func3():
    x = 1
    def func4():
        x = 5
        print(x)
    func4()

func3()


# Global
def func5():
    print(x)

x = 3
func5()

# Local
def func6():
    x = 9
    print(x)

func6()

# Built-in

from math import e

print(e)