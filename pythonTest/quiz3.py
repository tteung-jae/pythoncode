import re

class Student:
    studentlist = []

    page=1

    def firstinput(self):
        choice=input('''
            다음 중에서 하실 일을 골라주세요 :
            I - 학생 정보 입력
            U - 학생 정보 수정
            D - 학생 정보 삭제
            L - 학생 리스트
            Q - 프로그램 종료
            ''').upper()  
        return choice
    
    def exe(self,choice):
        if choice=='I':
            self.insertData()
            
        elif choice=='U':
            self.updateData()
        
        elif choice=='D':
            self.deleteData()
        
        elif choice=='L':
            self.listData()

        elif choice=='Q':
            quit()


    def insertData(self): 
        print("학생 정보 입력")
        while True: # 중복되지 않게 입력
            studentID = input("학번을 입력해주세요 : ")
            check = 0
            for i in self.studentlist:
                if i['학번'] == studentID:
                    check = 1
            if check == 0:
                break
            print('중복되는 학번이 있습니다.')

        name = input("학생 이름을 입력해주세요 : ")
        department = input("학과를 입력해주세요 : ")
        phonenum = input("전화번호를 입력해주세요 : ")
        address = input("주소를 입력해주세요 : ")
        
        student = {"학번":studentID,"이름":name,"학과":department,"전화번호":phonenum, "주소":address}
        self.studentlist.append(student)
        self.page += 1

        print(student)
        print(self.studentlist)

    def updateData(self): 
        print("학생 정보 수정")
        idx = -1
        choice1 = input("수정하려는 학생 정보의 학번을 입력하세요 : ")
        for i in range(0,len(self.studentlist)):
            if self.studentlist[i]['학번'] == choice1:
                while True:
                    choice2 = input('''
                    다음 중 수정할 정보를 입력해주세요
                    1. 이름(name) 2.학과(department) 3.전화번호(phonenum) 4.주소(address)
                    수정할 내용이 없으면 'exit'를 입력해주세요''')
                    if choice2 in ('1', '이름', 'name'):
                        self.studentlist[i]['이름'] = input("수정할 이름을 입력하세요 : ")
                    elif choice2 in ('2', '학과', 'department'):
                        self.studentlist[i]['학과'] = input("수정할 학과를 입력하세요 : ")
                    elif choice2 in ('3', '전화번호', 'phonenum'):
                        self.studentlist[i]['전화번호'] = input("수정할 전화번호를 입력하세요 : ")
                    elif choice2 in ('4', '주소', 'address'):
                        self.studentlist[i]['주소'] = input("수정할 주소를 입력하세요 : ")
                    elif choice2 == 'exit':
                        idx = 0
                        break
                    else:
                        print("잘못 입력하셨습니다.")
                if idx == 0:
                    break
        if idx == -1:
            print("등록되지 않은 학번입니다.")
    
    def deleteData(self):
        print("학생 정보 삭제")

        for i in self.studentlist:
            print(i['이름'],':',i['학번'],end="  ")
        print()

        choice1 = input("삭제하려는 고객 정보의 학번을 입력하세요.")
        delok = 0
        for i in range(0,len(self.studentlist)):
            if self.studentlist[i]['학번'] == choice1:
                print("{} 고객님의 정보가 삭제되었습니다." .format(self.studentlist[i]['학번']))
                del self.studentlist[i]
                delok = 1
            if delok == 1:
                break
        if delok == 0:
            print("등록되지 않은 학번입니다.")
        
        for i in self.studentlist:
            print(i['이름'],':',i['학번'],end="  ")
        print()
        self.page = len(self.studentlist) - 1

    def listData(self):
        print("학생 리스트")
        for i in self.studentlist:
            print(i)

    def __init__(self):
        while True:
            self.exe(self.firstinput())

Student()
