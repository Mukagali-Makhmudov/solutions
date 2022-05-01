# --- Л-е-с-о-п-о-с-а-д-к-и ---
forest = []
line = input()
while line:
    forest.append([int(x) for x in line.split(" : ")])
    line = input()
value = int(input())
for i in range(len(forest)):
    forest[i] = [x if x >= value else 0 for x in forest[i]]
    print(*forest[i], sep='\t')


# --- Д-и-а-г-о-н-а-л-и н-а-о-б-о-р-о-т ---
n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
result = 0
for i in range(n):
    matrix[i][i], matrix[i][len(matrix[i]) - i - 1] = matrix[i][len(matrix[i]) - i - 1], matrix[i][i]
    result += matrix[i][i] + matrix[i][len(matrix[i]) - i - 1]
for item in matrix:
    print(*item)
print(result)


# --- Л-е-в-ы-й с-ы-н п-р-а-в-ы-й с-ы-н ---
numbers = [int(x) for x in input().split()]
result = [numbers]
while len(numbers) > 1:
    numbers = [sum(numbers[i:i + 2]) for i in range(0, len(numbers), 2)]
    result.append(numbers)
for item in result[::-1]:
    print(*item)


# --- Т-р-а-н-с-п-о-н-и-р-о-в-а-н-и-е ---
n, m = int(input()), int(input())
array = []
for _ in range(n):
    array.append([input() for _ in range(m)])

result = [["_"] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        result[i][j] = array[j][i]
for item in array:
    print(*item, sep='; ')
print()
for item in result:
    print(*item, sep='; ')


# --- З-а-г-о-т-о-в-к-а ---
abc = "абвгдежзик"
field = [[0] * 10 for _ in range(10)]
for i in range(10):
    coord, direction = input().split()
    y, x = abc.index(coord[0]), int(coord[1:]) - 1
    if not i:
        if direction == "г":
            for j in range(y, y + 4):
                field[x][j] = "\u25A1"
        else:
            for j in range(x, x + 4):
                field[j][y] = "\u25A1"
    elif i in (1, 2):
        if direction == "г":
            for j in range(y, y + 3):
                field[x][j] = "\u25A1"
        else:
            for j in range(x, x + 3):
                field[j][y] = "\u25A1"
    elif i in (3, 4, 5):
        if direction == "г":
            for j in range(y, y + 2):
                field[x][j] = "\u25A1"
        else:
            for j in range(x, x + 2):
                field[j][y] = "\u25A1"
    else:
        field[x][y] = "\u25A1"
for item in field:
    print(*item)


# --- 8 р-и-ч-н-о-е у-м-н-о-ж-е-н-и-е ---
n, m = int(input()), int(input())
x, y = int(input()), int(input())
print('\t'.join([""] + [oct(x)[2:] for x in range(n, m + 1)]))
table = []
for i in range(n, m + 1):
    temp = [oct(i * x)[2:] for x in range(n, m + 1)]
    table.append(temp)
    print('\t'.join([oct(i)[2:]] + temp))
print(table[x][y])


# --- Р-а-м-к-а ---
n = int(input())
arr = []
for i in range(n):
    line = [int(x) for x in input().split()]
    arr.append(line)
result = 0
for i in range(n):
    for j in range(len(arr[i])):
        if i == 0 or i == n - 1 or j == 0 or j == len(arr[i]) - 1:
            result += arr[i][j]
arr[n // 2][len(arr[0]) // 2] = result
for item in arr:
    print(*item, sep='\t')


# --- С-л-о-в-а-р-н-а-я с-т-а-т-и-с-т-и-к-а ---
word = input()
result = []
while word:
    result.append([word.count(word[i]) for i in range(len(word))])
    word = input()
print(result)


# --- Д-о-р-о-г-и д-о-р-о-г-и ---
cities = set()
roads = []
line = input()
while line:
    cities.update(list(line))
    roads.append(line)
    line = input()
temp = sorted(cities)
print(' '.join(["", ""] + temp))
for item in temp:
    print(item, end=" ")
    print(*[1 if item + x in roads else 0 for x in temp])


# --- Х f-i-l-e-s ---
n = int(input())
files = [input().split() for _ in range(n)]
for i in range(1, n - 1):
    temp = []
    for j in range(1, len(files[0]) - 1):
        word = ''.join([files[i][j], files[i - 1][j - 1],
                        files[i - 1][j + 1], files[i + 1][j - 1],
                        files[i + 1][j + 1]])
        temp.append(word)
    print(*temp)