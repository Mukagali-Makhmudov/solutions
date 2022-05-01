# --- О-с-т-а-н-о-в-к-и ---
intervals = [int(x) for x in input().split()]
start, end = [int(x) for x in input().split()]
print(sum(intervals[start:end]))


# --- В т-р-е-х с-о-с-н-а-х ---
line = input()
print(line[line.find("сосна") + 6:line.rfind("сосна") - 1])


# --- Э-н-и-к-и б-э-н-и-к-и ---
letter, line = input(), input()
print(line.lower().count(letter.lower()))


# --- П-о-з-в-а-т-ь д-р-у-г-а ---
line = input()
lines = []
while line:
    lines.append(line)
    line = input()
name = input()
result = [line[len(name) + 2:].capitalize()
          for line in lines if line.startswith("@" + name)]
result.sort()
for item in result:
    print(item)


# --- С-к-а-ж-и п-о б-у-к-в-а-м ---
divisor, line = input(), input()
print(' '.join([divisor.join(list(word.upper())) for word in line.split()]))


# --- Б-ы-с-т-р-ы-й п-о-и-с-к д-е-л-и-т-е-л-е-й ---
n = int(input())
stack = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        print(i, end=' ')
        if (n // i) != i:
            stack.append(n // i)
while stack:
    print(stack.pop(), end=' ')


# --- И о-б-р-а-т-н-о ---
intervals = [int(x) for x in input().split()]
start, end = [int(x) for x in input().split()]

print(sum(intervals[start:end]) + sum(intervals[end:start]))


# --- П-а-л-о-ч-к-и и к-о-л-б-о-ч-к-и ---
s, luminosity = input(), int(input())
if luminosity > 100:
    s = s.replace("0000", "|||")
else:
    s = s.replace("|||", "00", 3)
s = s.replace("|0|", "|00|", 1)
print(s)


# --- П-е-р-с-п-е-к-т-и-в-а ---
houses = [int(x) for x in input().split()]
stack = []
local_max = 0
for height in houses:
    if height > local_max:
        stack.append(height)
        local_max = height
print(">>".join([str(x) for x in stack]))


# --- П-о-д-с-т-р-о-к-и ---
line = input()
result = []
for i in range(1, len(line) // 2):
    for j in range(len(line) - i):
        temp = line[j:j + i]
        n = line.count(temp)
        if n > 1 and (temp, n) not in result:
            result.append((temp, n))
for item in result:
    print(f"{item[0]}: {item[1]}")