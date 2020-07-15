import random
import time

operator=["+", "-", "//", "*"]
score = 0

input("계산 문제 게임시작(enter)")
start = time.time()

for x in range(3):
    a = random.randint(1,50)
    b = random.randint(1,50)
    op = random.choice(operator)

    print("%d %s %d" %(a, op, b))
    ans = int(input("= "))

    q = str(a) + op + str(b)
    
    if eval(q) == ans:
        print("정답")
        score += 1
    else:
        print("오답")

print("\n총 3문제 중 %d개 맞췄습니다." %score)
end = time.time()
et = end - start
print("총", int(et), "초 걸렸습니다.")
