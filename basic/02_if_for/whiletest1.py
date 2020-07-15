prompt = '''
-----------------------
    커피 자판기 메뉴
-----------------------
 1. 메뉴 리스트 확인
 2. 커피 메뉴 추가
 3. 커피 메뉴 삭제
 4. 커피 자판기 동작
 5. 종료
-----------------------
메뉴 선택 >>> '''

dic = {"아메리카노":2000, "에스프레소":2000, "카푸치노":2500, "카페라떼":2500, "아이스티":2000}

while True:
    print(prompt)
    menu = input()

    if menu == '1':
        print('''-------------------------------------
            커피 메뉴판 
-------------------------------------''')
        for (name, price) in dic.items():
            print("제품명 : {:}, 가격 : {:,}원" .format(name, price))

    elif menu == '2':
        print("커피 메뉴를 추가합니다.")
        name = input("메뉴 >> ")
        price = int(input("가격 >> "))
        dic[name]=price
        print("메뉴에 {} 제품이 {:,}원으로 추가되었습니다." .format(name,price))
        
    elif menu == '3':
        print("커피 메뉴를 삭제합니다.")
        name = input("삭제할 메뉴 >> ")
        # dic.pop(name) 로 하면 찍어주고 삭제.
        del dic[str(name)]
        print("커피 메뉴에서 '%s'가 삭제되었습니다." %name)
        print("<<< 메뉴 삭제 후 메뉴 리스트 >>>")
        print(dic)

    elif menu == '4':
        print("원하시는 커피를 입력해주세요.")
        name = input()
        if name not in dic:
            print("요청하신 제품은 저희 가게에 없어요ㅜㅜ")   
        else:
            print("'{}' 제품은 {:,}원입니다.\n돈을 넣어주세요." .format(name,dic[name]))
            money = int(input())
            print("{:,}원 받았습니다." .format(money))

            if int(dic[name]) <= money:
                print("'%s' 제품이 나갑니다~ 맛있게 드세요!" %name)
                print("남은 금액 {:,}원 받으시구요><" .format(money - int(dic[name])))
            else:
                print("금액이 부족해요ㅜㅜ")

    elif menu == '5':
        print("프로그램 종료.")
        break
