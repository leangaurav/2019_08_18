def f1():
    x = int(input())
    print("f1 finished")
    return x

def f2():
    try:
        x = f1()
        print(f"1/{x}", 1/x)
        print("f2 finished")
        return x
    except ValueError:
        print("Exception in f1")
        return 0

def f3():
    x = f2()
    print( "Index ", [1,2,3][x])
    print("f3 finished")
    
    """
except ValueError as e:
    print("Invalid input !!", e)
except (IndexError, ZeroDivisionError) as err:
    print("Zero/Index Error", err, type(err))
    """
try:
    f3()
except:
    print("Some exception")
print("end")