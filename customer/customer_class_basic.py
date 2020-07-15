import re

class Customer:
    custlist=[{"이름":'김승재',"성별":'M',"이메일":"tmd0212@naver.com","출생년도":1995},
            {"이름":"김진범","성별":"M","이메일":"qja1234@naver.com","출생년도":1995},
            {"이름":"박병건","성별":"F","이메일":"rjs4567@naver,com","출생년도":1995},
            {"이름":"김병길","성별":"M","이메일":"rlf789@naver.com","출생년도":1993}]
    page=3

    def firstinput(self):
        choice=input('''
            다음 중에서 하실 일을 골라주세요 :
            I - 고객 정보 입력
            C - 현재 고객 정보 조회
            P - 이전 고객 정보 조회
            N - 다음 고객 정보 조회
            U - 고객 정보 수정
            D - 고객 정보 삭제
            Q - 프로그램 종료
            ''').upper()  
        return choice
    
    def exe(self,choice):
        if choice=='I':
            self.insertData()
            
        elif choice=='C':
            self.curSearch()
        
        elif choice=='P':
            self.preSearch()

        elif choice=='N':
            self.nextSearch()

        elif choice=='U':
            self.updateData()
        
        elif choice=='D':
            self.deleteData()
        
        elif choice=='Q':
            quit()



    def insertData(self): 
        print("고객 정보 입력")
        name = input("이름을 입력해주세요 : ")

        while True:
            gender = input("성별(M/m 또는 F/f)을 입력해주세요 : ")
            gender = gender.upper()
            if gender == 'M' or gender == 'F':
                break
            else:
                print("성별을 잘못입력하셨습니다")
            
        while True: # 중복되지 않게 입력
            email = input("이메일을 입력해주세요 : ")
            p = re.compile('[a-zA-Z][a-zA-Z0-9]{4,}@[a-z]{2,}[.][a-z]{2,5}')
            result = p.match(email)
            if result == None:
                print("'@'를 포함한 정확한 이메일을 입력해주세요")
            else:
                check = 0
                for i in self.custlist:
                    if i['이메일'] == email:
                        check = 1
                if check == 0:
                    break
                print('중복되는 이메일이 있습니다.')

        while True:
            birthyear = input("출생년도를 입력해주세요(4자리) : ")
            if len(birthyear) == 4 and birthyear.isdecimal():
                birthyear = int(birthyear)
                break
            else:
                print("다시 입력해주세요")
        
        customer = {"이름":name,"성별":gender,"이메일":email,"출생년도":birthyear}
        self.custlist.append(customer)
        self.page += 1

        print(customer)
        print(self.custlist)
        print(self.page)
        
    def curSearch(self):
        print("현재 고객 정보 조회")
        if self.page >= 0:
            print("현재 페이지는 {}쪽 입니다." .format(self.page+1))
            print(self.custlist[self.page])
        else:
            print("입력된 정보가 없습니다.")

    def preSearch(self):
        print("이전 고객 정보 조회")
        if self.page <= 0:
            print("첫번째 페이지이므로 이전 페이지로 이동이 불가합니다.")
        else:
            self.page -= 1
            print("현재 페이지는 {}쪽 입니다." .format(self.page+1))
            print(self.custlist[self.page])

    def nextSearch(self):
        print("다음 고객 정보 조회")
        if self.page >= len(self.custlist)-1:
            print("마지막 페이지이므로 다음 페이지로 이동이 불가합니다.")
        else:
            self.page += 1
            print("현재 페이지는 {}쪽 입니다." .format(self.page+1))
            print(self.custlist[self.page])

    def deleteData(self):
        print("고객 정보 삭제")

        for i in self.custlist:
            print(i['이름'],':',i['이메일'],end="  ")
        print()

        choice1 = input("삭제하려는 고객 정보의 이메일을 입력하세요.")
        delok = 0
        for i in range(0,len(self.custlist)):
            if self.custlist[i]['이메일'] == choice1:
                print("{} 고객님의 정보가 삭제되었습니다." .format(self.custlist[i]['이메일']))
                del self.custlist[i]
                delok = 1
            if delok == 1:
                break
        if delok == 0:
            print("등록되지 않은 이메일입니다.")
        
        for i in self.custlist:
            print(i['이름'],':',i['이메일'],end="  ")
        print()
        self.page = len(self.custlist) - 1

    def updateData(self): 
        print("고객 정보 수정")
        choice1 = input("수정하려는 고객 정보의 이메일을 입력하세요.")
        idx = -1
        for i in range(0,len(self.custlist)):
            if self.custlist[i]['이메일'] == choice1:
                while True:
                    choice2 = input('''
                    다음 중 수정할 정보를 입력해주세요
                    1. 이름(name) 2.성별(gender) 3.출생년도(birthyear)
                    수정할 내용이 없으면 'exit'를 입력해주세요''')
                    if choice2 in ('1', '이름', 'name'):
                        self.custlist[i]['이름'] = input("수정할 이름을 입력하세요")
                    elif choice2 in ('2', '성별', 'gender'):
                        while True:
                            self.custlist[i]['성별'] = input("수정할 성별(M/m 또는 F/f)을 입력하세요")
                            self.custlist[i]['성별'] = self.custlist[i]['성별'].upper()
                            if self.custlist[i]['성별'] == 'M' or self.custlist[i]['성별'] == 'F':
                                break
                            else:
                                print("성별을 잘못입력하셨습니다")
                    elif choice2 in ('3', '출생년도', 'birthyear'):
                        while True:
                            self.custlist[i]['출생년도'] = input("수정할 출생년도를 입력하세요(4자리)")
                            if len(self.custlist[i]['출생년도']) == 4 and self.custlist[i]['출생년도'].isdecimal():
                                self.custlist[i]['출생년도'] = int(self.custlist[i]['출생년도'])
                                break
                            else:
                                print("다시 입력해주세요")
                    elif choice2 == 'exit':
                        idx = 0
                        break
                    else:
                        print("잘못 입력하셨습니다.")
                if idx == 0:
                    break
        if idx == -1:
            print("등록되지 않은 이메일입니다.")

    def __init__(self):
        while True:
            self.exe(self.firstinput())

Customer()
