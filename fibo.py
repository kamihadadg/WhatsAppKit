def fibo(n):
    fibo_list = []
    for i in range(n):
        fibo_list.append(_fibonacci(i))
    return fibo_list

def _fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return _fibonacci(n - 1) + _fibonacci(n - 2)

def kmfibo(n):
    fibo_list = []
    a, b = 0, 1
    for i in range(n):
        if i == 0 or i == 1:
            c = i
        else:
            c = a + b
            a, b = b, c
        fibo_list.append(c)
    return fibo_list

# Example: Print Fibonacci numbers up to index 20
Listcount = 20
print(f"Fibo: {fibo(Listcount)}")
print(f"KMFibo: {kmfibo(Listcount)}")
