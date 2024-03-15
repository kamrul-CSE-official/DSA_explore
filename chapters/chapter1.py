
def firsttype():
    n = input()
    n = int(n)
    result = n * (n + 1) / 2
    print(result)

def secondtype():
    n = input()
    n = int(n)
    result = 0
    for i in range(1, n + 1):
        result = result + i
    print(result)