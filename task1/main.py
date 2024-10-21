def caching_fibonacci():
    'Function to get fibonnaci number with cache'
    cache = {}
    def fibonacci(n):
        'Function to get fibonnaci number from cache'
        if n in {0, 1}:
            return n  
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
    return fibonacci

fib = caching_fibonacci() #Test
print(fib(10)) #Test
print(fib(15)) #Test
print(fib(678)) #Test
#EOF