# --- П-р-я-т-к-и ---
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
m = int(input())
for _ in range(m):
    name = input()
    for i in range(n):
        if name in lines[i]:
            print(i + 1)
            break
    else:
        print(-1)

# --- Т-о-л-ь-к-о к-р-а-т-н-ы-е ---
number = int(input())
sequence = []
while number:
    sequence.append(number)
    number = int(input())
result = []
for item in sequence:
    if item % len(sequence) == 0:
        result.append(item)
print(result)

# --- В-с-е р-а-в-н-ы ---
line = input()
lines = []
max_length = len(line)
while line:
    lines.append(line)
    max_length = max(max_length, len(line))
    line = input()
for line in lines[::-1]:
    n = (max_length - len(line)) // 2
    print("-" * n +
          line + "-" * (max_length - len(line) - n))

# --- Н-а с-в-о-е-м м-е-с-т-е ---
n = int(input())
line = []
for _ in range(n):
    line.append(input())
word = input()
ind = 0
for i in range(n):
    if word < line[i]:
        print(i)
        break
else:
    print(n)

# --- П-р-я-т-к-и 2 ---
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
m = int(input())
name = []
for _ in range(m):
    name.append(input())
for i in range(n):
    for word in name:
        if word not in lines[i]:
            break
    else:
        print(lines[i])

# --- Ф-л-а-г-и ---
flags = []
m = int(input())
for _ in range(m):
    flags.append(input())
n = int(input())
for i in range(n):
    print(flags[i % m])

# --- К-а-м-у-ш-к-и ---
n = int(input())
numbers = []
res = 0
for _ in range(n):
    x = int(input())
    numbers.append(x)
    res += x
result = i = 0
while i < len(numbers):
    if numbers[i] % 2 != res % 2:
        result += numbers[i]
        del numbers[i]
    else:
        i += 1
print(result, numbers)

# --- П-о-д-а-р-к-и д-л-я д-е-т-е-й ---
n = int(input())
names = []
for _ in range(n):
    names.append(input())
m = int(input())
gifts = []
for _ in range(m):
    name = input()
    if name in names and name not in gifts:
        print("Вот твой подарок,", name + "!")
        gifts.append(name)
    else:
        print(name + ", всем по одному подарку!")

# --- Л-о-в-у-ш-к-а д-л-я с-н-о-в ---
dreams = []
dream = input()
while dream:
    dreams.append(dream)
    dream = input()
n, m = int(input()), int(input())
result = ''
for line in dreams[n - 1:m]:
    if len(line) > len(result):
        result = line
print(result)

# --- П-р-о-с-т-е-н-ь-ки-й п-а-р-с-и-н-г ---
lines = []
line = input()
while line != "</html>":
    if "<p>" in line:
        temp = line[3:]
        if "</p>" in temp:
            temp = temp[:-4]
        else:
            line = input()
            while "</p>" not in line:
                temp += " " + line
                line = input()
            temp += " " + line[:-4]
        lines.append(temp)
    line = input()
for line in lines[::-1]:
    print(line)