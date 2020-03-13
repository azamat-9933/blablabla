f1 = 1
f2 = 1
sum = 0
count = 0
while sum < 4000000:
    if sum % 2 == 1:
        count+=sum
    sum = f1 + f2
    f1 = f2
    f2 = sum
print(count + 2)