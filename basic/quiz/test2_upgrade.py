import random, time, pickle, json

with open("./basic/quiz/word.json", "rt") as f:
    q = json.load(f)

with open('./basic/quiz/rank.json', 'rt') as f:
    rank = json.load(f)

while True:
    print('''
    1.타자게임 
    2.문제불러오기 
    3.문제저장하기 
    4.문제 등록 수정 삭제 
    5.등수 
    6.종료하기''')
    menu = input("메뉴를 선택하세요\n")
    if menu == "1":
        n = 1
        quiz = random.choice(q)
        input("타자연습 시작(enter)")
        start = time.time()

        while n <= 5:
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
        name = input("사용자 이름을 입력하세요")
        rank[name] = float(end - start)
        print(rank)
    
    elif menu == "2":
        # pickle 파일 불러오기
        # f = open("./basic/quiz/word.pickle", "rb")
        # q1 = pickle.load(f)
        # f.close()
        # print(q1)

        # json 파일 불러오기
        with open("./basic/quiz/word.json", "rt") as f:
            q1 = json.load(f)

    elif menu == "3":
        # pickle로 저장하기
        # f = open("./basic/quiz/word.pickle", 'wb')
        # pickle.dump(q, f)
        # f.close()

        # json으로 저장하기
        with open('./basic/quiz/word.json', 'wt') as f:
            json.dump(q, f, indent=4)

    elif menu == "4":
        while True:
            select = input("1.문제 등록 2.문제 수정 3.문제 삭제 4.종료\n")
            if select == '1':
                print(q)
                add = input("추가할 문제를 입력하세요")
                q.append(add)
                print(q)
            elif select == '2':
                print(q)
                change = input("어떤 문제를 수정하나요?")
                index = q.index(change)
                change = input("수정내용 입력")
                q[index] = change
                print(q)
            elif select == '3':
                print(q)
                delete = input("삭제할 문제를 입력하세요")
                q.remove(delete)
                print(q)
            elif select == '4':
                break
            else:
                print("메뉴를 잘못 선택하셨습니다")

    elif menu == "5":
        ranklist = sorted(rank.items(), key=lambda x:x[1])
        num = 1
        for k, v in ranklist:
            print("%d등 %s %f" %(num, k, v))
            num += 1

    elif menu == "6":
        print("프로그램 종료.")
        with open('./basic/quiz/rank.json', 'wt') as f:
            json.dump(rank, f, indent=4)
        break
    else:
        print("메뉴를 잘못 선택하셨습니다.")

