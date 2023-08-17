def calc(a, b):
    def add(a, b):
        c = a + b
        print(f"{a} and {b} add vlaue is: ", c)
        return c

    def sub(a, b):
        c = a - b
        print(f"{a} and {b} sub vlaue is: ", c)
        return c

    def mul(a, b):
        c = a * b
        print(f"{a} and {b} mul vlaue is: ", c)
        return c

    def div(a, b):
        c = a / b
        print(f"{a} and {b} div vlaue is: ", c)
        return c

    def mod(a, b):
        c = a % b
        print(f"{a} and {b} mode vlaue is: ", c)
        return c

    d = add(a, b)
    e = sub(a, b)
    f = mul(a, b)
    g = div(a, b)
    h = mod(a, b)

    return d, e, f, g, h


a = int(input("Enter your A Number:"))
b = int(input("Enter your B Number:"))
value = calc(a, b)
print(list(value))

