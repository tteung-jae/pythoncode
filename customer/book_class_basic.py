import re

class Book:
    booklist=[
    ]
    no=0

    def firstinput(self):
        choice=input('''
            다음 중에서 하실 일을 골라주세요 :
            1. 책 등록하기
            2. 리스트 출력
            3. 수정하기
            4. 삭제하기
            5. 종료
            ''').upper()  
        return choice
    
    def exe(self,choice):
        if choice == "1":        
            self.insertData()
        elif choice == "2":
            self.curSearch()
        elif choice == '3':
            self.updateData()
        elif choice == '4':
            self.deleteData()
        elif choice == "5":
            quit()



    def insertData(self): 
        print("책 등록하기")
        book = {"일련번호":"", "제목":"", "출판사":"", "지은이":"", "가격":""}
        self.no += 1
        book['일련번호'] = self.no
        book['제목'] = str(input("책 제목을 입력해주세요 : "))
        book['출판사'] = str(input("출판사를 입력해주세요 : "))
        book['지은이'] = str(input("지은이를 입력해주세요 : "))
        book['가격'] = input("가격을 입력해주세요 : ")
        book['일련번호'] = str(book['일련번호'])
        self.booklist.append(book)
        print(book)
        print(self.booklist)
        
    def curSearch(self):
        print('''-------------------------------------
            Book List
-------------------------------------''')
        for a in self.booklist:
            print(a)

    def deleteData(self):
        print("책 삭제하기")
    
        for i in self.booklist:
            print(i["일련번호"], ":", i["제목"], end="\n")
            print()

        choice1 = input("삭제하려는 책의 일련번호를 입력하세요.")
        delok = 0
        for i in range(0, len(self.booklist)):
            if self.booklist[i]['일련번호'] == choice1:
                print('{} 번의 도서 정보가 삭제되었습니다.' .format(self.booklist[i]['일련번호']))
                del self.booklist[i]
                delok = 1
            if delok == 1:
                break
        if delok == 0:
            print("등록되지 않은 일련번호입니다.")
        self.no = len(self.booklist) - 1

    def updateData(self): 
        print("책 수정하기")
        print(self.booklist)
        while True:
            for i in self.booklist:
                print(i["일련번호"], ":", i["제목"], end="\n")
            print()

            choice1 = input("수정하려는 책의 일련번호를 입력하세요.")
            idx = -1
            for i in range(0, len(self.booklist)):
                if self.booklist[i]['일련번호'] == choice1:
                    idx = i
            if idx == -1:
                print("등록되지 않은 일련번호입니다.")
                break
            choice2 = input('''
            다음 중 수정하실 정보를 선택해주세요.
            1.제목 2.출판사 3.지은이 4.가격
            (수정할 정보가 없으면 'exit'를 입력)
            ''')
            if choice2 in ("제목", "출판사", "지은이", "가격"):
                self.booklist[idx][choice2] = input('수정할 {}을 입력하세요' .format(choice2))
                for i in self.booklist:
                    print(i["일련번호"], ":", i["제목"], end="\n")
                print()
                break
            elif choice2 == 'exit':
                break
            else: 
                print("존재하지 않은 일련번호입니다.")
                break

    def __init__(self):
        while True:
            self.exe(self.firstinput())

Book()
