import math

expression = "#4+1+3+#10000+5+81+#9+1"
cnt = 0
location = []
found = 0
oldstr = ''
newstr = ''

# print(expression)
for char in expression:

    if char == '#':
        found = 1
        # oldstr = oldstr+char

    elif found == 1 and char not in {'+', '-', '*', '/'}:
        location.append(cnt)
        # oldstr = oldstr+char

    elif found == 1 and char in {'+', '-', '*', '/'}:
        found = 0
        location.append('.')

    else:
        pass
    cnt += 1
# print(location)

if location==[]:
    pass
else:
    x=location.pop()
    if x !='.':
       location.append(x)
       location.append('.')
    else:
       location.append(x)


# print(location)

sv = []
rs = ''
count = 0
exp = expression
for n in location:
    if n != '.':
        rs = rs + expression[n]

    else:
        sv.append(math.sqrt(float(rs)))
        olds = '#' + rs
        exp = exp.replace(olds, str(sv[count]), 1)
        rs = ''
        count = count + 1

expression = exp

print(expression)
