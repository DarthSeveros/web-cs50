#A decorator is way of modificate a function, we take a function as input and we return a modificated 
#version of it

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello world!")

hello()