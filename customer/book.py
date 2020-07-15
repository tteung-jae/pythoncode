import bookFunc

booklist=[
]

no=0
def exe(choice, no):
    if choice == "1":        
        no = bookFunc.insertData(no, booklist)
        print(no)
    elif choice == "2":
        bookFunc.curSearch(no, booklist)
    elif choice == '3':
        bookFunc.updateData(booklist)
    elif choice == '4':
        bookFunc.deleteData(booklist)
    elif choice == "5":
        quit()
    return no

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    1. 책 등록하기
    2. 리스트 출력
    3. 수정하기
    4. 삭제하기
    5. 종료
    ''').upper()  

    no = exe(choice, no)
