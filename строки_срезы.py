# --- П-о-п-а-р-н-о ---
line = input()
while line:
    print(line[:2])
    line = line[2:]


# --- П-о м-е-с-т-а-м ---
line = input()
print(len(set(line[1::2])))


# --- Р-а-з-в-о-р-о-т ---
line = input()
n, m, k = int(input()), int(input()), int(input())
print(line[n:m:-k])


# --- Д-л-и-н-н-о-е с-л-о-в-о ---
line = input()
res = ""
longest = ""
ind = 0
for i in range(len(line)):
    if line[i] == ' ' and not res:
        res = line[ind:i]
        if len(res) > len(longest):
            longest = res
        res = ''
    elif line[i] != ' ' and line[i - 1] == ' ':
        ind = i
res = line[ind:len(line)]
if len(res) > len(longest):
    longest = res
print(longest)



# --- Д-р-о-в-о-с-е-к ---
line = input()
n = int(input())
while line:
    k = len(line) - n if len(line) >= n else 0
    print(line[k:])
    line = line[:-n]
    if line:
        print(line[:n])
        line = line[n:]



# --- А-м-е-р-и-к-а-н-с-к-и-й ф-о-р-м-а-т ---
number = input()
res = "+1(" + number[:3] + ")" + number[3:6] + "-" + number[6:]
print(res)


# --- Д-о и п-о-с-л-е ---
line = input()
ind = 0
for i in range(len(line)):
    if line[i] == '-':
        ind = i
        break
print(line[ind + 1:] + line[ind] + line[:ind])



# --- Т-у-д-а и о-б-р-а-т-н-о ---
line = input()
print(line == line[::-1])



# --- Т-у-д-а и о-б-р-а-т-н-о 2 ---
line = input()
res = ''
for symbol in line:
    if symbol != ' ':
        res += symbol
print(res == res[::-1])


# --- Х-о-р-о-ш-о у-м-е-т-ь ч-и-т-а-т-ь ---
sentence = input()
familiar = 'ESM'
unnown = set()
index_familiar = next_familiar = 0
for i in range(len(sentence)):
    if sentence[i] in familiar and not index_familiar:
        index_familiar = i + 1
    elif sentence[i] in familiar and index_familiar and \
            not next_familiar:
        next_familiar = i + 1
    elif sentence[i] not in familiar and sentence[i] != ' ':
        unnown.add(sentence[i])
print(index_familiar)
if next_familiar and index_familiar:
    print(next_familiar - index_familiar - 1)
elif index_familiar:
    print(len(sentence) - index_familiar)
else:
    print(len(sentence))
print(len(unnown))



# --- С-д-в-и-г ---
line1, line2 = input(), input()
for i in range(len(line2)):
    if line2[i:] + line2[:i] == line1:
        print(i)
        break
else:
    print("NO")



# --- С п-е-р-в-о-г-о д-о п-о-с-л-е-д-н-е-г-о ---
symbol, line = input(), input()
start = stop = -1
for i in range(len(line)):
    if line[i] == symbol:
        if start == -1:
            start = i
        else:
            stop = i
if start == -1 or stop == -1:
    stop = len(line)
print(line[start + 1:stop])



# --- С-с-ы-л-к-и н-а и-с-т-о-ч-н-и-к ---
text = input()
while "[" in text:
    ind = -1
    for i in range(len(text) - 1):
        if text[i] == "[":
            ind = i
        elif text[i] == "]":
            text = text[:ind] + text[i + 1:]
            ind = -1
            break
    if ind != -1:
        text = text[:ind]
print(text)


# --- С-л-о-в-а д-л-я к-а-д-а-в-р-а ---
template = input()
vowels = 'аяоёуюэеиы'
line = input()
no_words = True
while line:
    flag = True
    if '*' not in template:
        if len(line) != len(template):
            line = input()
            continue
        else:
            for i in range(len(line)):
                if template[i] == '1' and line[i] not in vowels or \
                        template[i] == '0' and line[i] in vowels or \
                        template[i] == '?':
                    continue
                else:
                    flag = False
                    break
    else:
        star_index = template.index('*')
        temp_start = template[:star_index]
        line_start = line[:star_index]
        temp_last = template[-1:star_index:-1]
        line_last = line[-1:len(line) - len(temp_last) - 1:-1] if \
            len(line) >= len(template) - 1 else line[-1]
        if len(temp_start) != len(line_start) or \
                len(temp_last) != len(line_last):
            line = input()
            continue
        else:
            for i in range(len(temp_start)):
                if temp_start[i] == '1' and line_start[i] not in vowels or \
                        temp_start[i] == '0' and line_start[i] in vowels or \
                        temp_start[i] == '?':
                    continue
                else:
                    flag = False
                    break
            for i in range(len(line_last)):
                if temp_last[i] == '1' and line_last[i] not in vowels or \
                        temp_last[i] == '0' and line_last[i] in vowels or \
                        temp_last[i] == '?':
                    continue
                else:
                    flag = False
                    break
    if flag:
        no_words = False
        print(line)
    line = input()
if no_words:
    print('Есть нечего, значить!')
