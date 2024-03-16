
n = input()
n = int(n)
count = 0

for i in range(n):
    count += 1
for i in range(n):
    for j in range(n):
        count += 1
print("Count value", count)

def average(l):
    if not l:
        return None
    return sum(l) / len(l)
if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    print(average(l))

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

