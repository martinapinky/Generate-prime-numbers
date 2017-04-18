def generateprimenumbers(n):
    primenumbers = []

    if isinstance(n, int):
        for x in range(0, n + 1):
            if x < 2:
                r = 0
            else:
                i = 2
                while i < x:
                    if x % i == 0:
                        break
                    i = i + 1
                else:
                    primenumbers.append(x)

    return primenumbers

print(generateprimenumbers(9))