import random, time

q=["love", "대한민국", "사랑의 시작은 고백에서부터", "파이썬", "python"]

n=1
quiz = random.choice(q)
input("타자연습 시작(enter)")
start = time.time()

while n <= 5 :
    print("{}번" .format(n))
    print(quiz)
    ans = input()

    if quiz == ans:
        print("정답!")
        n += 1
        quiz = random.choice(q)
    else:
        print("오답! 다시 시도!")

end = time.time()
print("총 {:.0f}초 걸렸습니다." .format(end - start))


