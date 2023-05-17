n = int(input())
p = list(map(int, input().split()))
sum2 = 0
p = sorted(p)
for i in range(n):  # i = 0,1,2,3,4
    sum1 = sum(p[0 : i + 1])
    sum2 += sum1
print(sum2)
