# --- П-а-л-е-о-н-т-о-л-о-г-и-я ---
eras = {"Archaea": (2800, 4500),
        "Proterozoic": (635, 2800),
        "Paleozoic": (300, 635),
        "Mesozoic": (145, 300),
        "Cenozoic": (0, 145)}

data = input()
while data:
    print([era for era in eras if eras[era][0] <= int(data) // 1000 < eras[era][1]][0])
    data = input()


# --- О-р-н-и-т-о-л-о-г-и-я ---
dic = {}
bird = input()
while bird:
    name, amount = bird.split(": ")
    dic[name] = dic.get(name, 0) + int(amount)
    bird = input()
print(dic)


# --- С-п-е-к-т-р-о-с-к-о-п ---
spectrum = {}
temp = input()
while temp:
    element, *lines = temp.split()
    spectrum[element] = lines
    temp = input()

data = []
line = input()
while line:
    data.append(line)
    line = input()
result = []
for item in spectrum:
    for line in spectrum[item]:
        if line not in data:
            break
    else:
        result.append(item)
print(*result, sep='\n')


# --- Р-а-з-н-ы-е ц-в-е-т-а ---
n = int(input())
picture = [input().split('\t') for _ in range(n)]
colors = {}
for item in picture:
    for color in item:
        colors[color] = colors.get(color, 0) + 1
result = [(item[1], item[0]) for item in colors.items()]
result.sort()
count = result[-1][0]
for item in result:
    if item[0] == count:
        print(item[1])
print(result)


# --- Х-а-р-а-к-т-е-р-и-с-т-и-к-и д-в-о-и-ч-н-ы-х ч-и-с-е-л ---
numbers = [int(x) for x in input().split()]
result = []
for number in numbers:
    temp = {'digits': 0, 'units': 0, 'zeros': 0}
    while number:
        d = number % 2
        if d:
            temp['units'] += 1
        else:
            temp['zeros'] += 1
        temp['digits'] += 1
        number //= 2
    result.append(temp)
print(result)


# --- С-е-р-т-и-ф-и-к-а-т-ы ---


# --- Г-д-е г-л-у-б-ж-е ---


# --- С-м-у-з-и ---


# --- О-п-о-з-д-а-н-и-е ---