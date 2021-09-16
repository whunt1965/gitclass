def say_hello():
    print("Hello World!")

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

if __name__=="__main__":
    say_hello()
    print("The sum of 1 and 2 is", add(1, 2))
    print("The difference of 1 and 2 is", subtract(1, 2))