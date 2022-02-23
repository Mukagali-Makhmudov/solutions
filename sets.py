# --- Католог ---
n = int(input())
res = set()
for _ in range(n):
    line = input()
    if line in res:
        print("ДА")
    else:
        print("НЕТ")
    res.add(line)


# --- QR - код ---
s = set()
ident = input()
while ident:
    s.add(ident)
    ident = input()
ident = input()
while ident:
    s.add(ident)
    ident = input()
ident = input()
while ident:
    s.add(ident)
    ident = input()
n = int(input())
res = set()
for _ in range(n):
    line = input()
    if line in s:
        res.add(line)
for item in res:
    print(item)


# --- Экономия ---
n = int(input())
res = set()
for _ in range(n):
    res.update(input())
print(len(res))


# --- Общие буквы ---
line1, line2, line3 = set(input()), set(input()), set(input())
result = line1.intersection(line2).union(
    line1.intersection(line3)).union(
    line2.intersection(line3))
for letter in result:
    print(letter, end='')


# --- Оркестр ---
set_1, set_2, set_3 = set(), set(), set()
line = input()
while line:
    set_1.add(line)
    line = input()
line = input()
while line:
    set_2.add(line)
    line = input()
line = input()
while line:
    set_3.add(line)
    line = input()
common = set_1.union(set_2).union(set_3) - set_1.intersection(set_2) - \
    set_1.intersection(set_3) - set_2.intersection(set_3)
for item in common:
    print(item)


# --- Все цифры ---
n = input()
digits = '0123456789'
for item in set(digits) - set(n):
    print(item, end=' ')


# --- Прививки ---
n = int(input())
set_1 = set()
for _ in range(n):
    set_1.add(input())
m = int(input())
set_2 = set()
for _ in range(m):
    set_2.add(input())
for item in set_1.intersection(set_2):
    print(item)


# --- Многоножки ---
n = int(input())
set_1 = set()
set_2 = set()
set_3 = set()
for _ in range(n):
    n = int(input())
    if n > 40:
        set_1.add(n)
    if n % 2 == 0:
        set_2.add(n)
    if n % 3 == 0:
        set_3.add(n)
result = set_1.intersection(set_2).union(set_1.intersection(set_3)).union(
    set_2.intersection(set_3)) - set_1.intersection(set_2).intersection(set_3)
for item in result:
    print(item, end=' ')


# --- Неплоские миры ---
worlds = int(input())
whole_comp = set()
for i in range(worlds):
    count_components = int(input())
    for _ in range(count_components):
        whole_comp.add(input())

for item in whole_comp:
    print(item)