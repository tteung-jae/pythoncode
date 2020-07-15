str1 = "abcdefgh"
list1 = [1,2,3,4,5,6]
tuple1 = (1,2,3,4,5,6)
dic1 = {1:"첫번째", 2:"두번째"}
set1 = {1,2,3,4}

for i in range(1,10):
    for j in range(2,10):
        print("{} X {} = {:2}" .format(j, i, i * j), end="   ")
    print()

a = [1,2,3,4,5]
result = [num*3 for num in a if num % 2 == 0]
print(result)

result = []
for num in a:
    if num % 2 == 0 :
        result.append(num*3)
print(result)