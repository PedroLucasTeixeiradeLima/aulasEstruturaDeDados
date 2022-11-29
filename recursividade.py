def fatorial(n):
  if n == 0:
    return 1
  return n * fatorial(n-1)

#print(fatorial(5))


def fibonacci(a, a2, n):
  if n>0:
    f = a + a2
    print(f)
    fibonacci(f, a, n-1)

fibonacci(1, -1, 10)



