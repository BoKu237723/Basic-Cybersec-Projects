def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculate(calc, n1, n2):
    return calc(n1, n2)

# result = calculate(div, 10,4) #this is decorator function
# print(result)


# ===========================================================================

def out():
    print("outside function")

    a = 1

    def inner():
        print("inner function")

    if a - 0 == 1:
        inner()

    # inner() calling inner from out function

# inner() # this cannot inner function directly

out()

