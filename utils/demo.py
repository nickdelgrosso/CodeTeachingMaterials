# developer code


def calculator(
    x, 
    y, 
    fun=lambda x, y: x + y,
):
    return fun(x, y)


# user code
def mul(x, y):
    return x * y

print(calculator(3, 4, mul))
print(help(calculator))