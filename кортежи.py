# --- З-а-д-а-ч-а д-в-у-х т-е-л ---
dist, force = int(input()), int(input())
n = int(input())
for i in range(n):
    r = int(input())
    print(("№" + str(i + 1), force * dist ** 2 / r ** 2))

# --- А-х-и-л-л-е-с и ч-е-р-е-п-а-х-а ---
result = []
number = int(input())
while number:
    result.append(number)
    number = int(input())
for i in range(len(result) - 1):
    for j in range(len(result) - 1 - i):
        if result[j] < result[j + 1]:
            result[j], result[j + 1] = result[j + 1], result[j]
for i in range(len(result) - 1):
    print(result[i], end='->')
print(result[-1])

# --- Г-р-о-з-а ---
n = int(input())
result = []
for _ in range(n):
    height, iron = int(input()), float(input())
    result.append((height, iron))
for i in range(n):
    for j in range(i + 1, n):
        if result[i][0] < result[j][0] or result[i][0] == result[j][0] and \
                result[i][1] < result[j][1]:
            result[i], result[j] = result[j], result[i]
for item in result:
    print(item)

# --- З-о-л-о-т-а-я р-ы-б-к-а ---
result = []
line = input()
while line != "разбитое корыто":
    result.append(line)
    line = input()
for i in range(len(result)):
    for j in range(i + 1, len(result)):
        if len(result[i]) > len(result[j]):
            result[i], result[j] = result[j], result[i]
for item in result:
    print(item)

# --- С-т-а-р-и-к и м-о-р-е ---
n = int(input())
waves = []
for i in range(n):
    line = input()
    waves.append((i + 1, line[:-2], int(line[-1])))
for i in range(n - 1):
    if waves[i][-1] < waves[i + 1][-1]:
        print(tuple(waves[i][:2]))

# --- С-т-а-р-и-к и л-о-д-к-а ---
n = int(input())
for i in range(n):
    line = input()
    for j in range(1, len(line)):
        if line[j] < line[j - 1]:
            print((i, j))

# --- С-т-а-р-и-к и р-ы-б-а ---
fishes = []
fish = input()
while fish:
    fishes.append(fish)
    fish = input()
by_abc = fishes[:]
by_len = fishes[:]
for i in range(len(fishes) - 1):
    for j in range(len(fishes) - 1 - i):
        if by_abc[j] > by_abc[j + 1]:
            by_abc[j], by_abc[j + 1] = by_abc[j + 1], by_abc[j]
        if len(by_len[j]) > len(by_len[j + 1]):
            by_len[j], by_len[j + 1] = by_len[j + 1], by_len[j]
if by_abc == by_len:
    print("YES")
else:
    for i in range(len(fishes)):
        if by_abc[i] != by_len[i]:
            print(by_abc[i], by_len[i])
            break

# --- Д-в-о-й-н-о-й ф-а-к-т-о-р-и-а-л ---
n = int(input())
result = [(0, 1)]
mul_odd = mul_even = 1

for i in range(1, n + 1):
    if i % 2:
        mul_odd *= i
        result.append((i, mul_odd))
    else:
        mul_even *= i
        result.append((i, mul_even))
print(result)

# --- Б-и-с-т-р-о ---
n = int(input())
result = []
orders = set()
for i in range(n):
    s = input()
    if s in orders:
        for item in result:
            if s == item[1]:
                item[0] += 1
    else:
        orders.add(s)
        result.append([1, s])
for item in result:
    print(tuple(item))