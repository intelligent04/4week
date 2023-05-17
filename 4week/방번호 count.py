n1 = input()
li = []
for p in range(10):
    li.append(n1.count(str(p)))
if max(li) == li[6] or max(li) == li[9]:
    a = (li[6] + li[9]) / 2
    a += 0.1
    print(round(a))
else:
    print(max(li))
