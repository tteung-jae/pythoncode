import customerFunc

custlist=[{'이름': '김승재', '성별': 'M', '이메일': 'tmd0212@naver.com', '출생년도': 1995},
{'이름': '김진범', '성별': 'M', '이메일': 'qja465@naver.com', '출생년도': 1995},
{'이름': '박병건', '성별': 'M', '이메일': 'qudrjs798@naver.com', '출생년도': 1995}]
page = 2

def exe(choice, page):
    if choice=='I':
        page = customerFunc.insertData(page, custlist)
        print(page)
    
    elif choice=='C':
        customerFunc.curSearch(page, custlist)
    
    elif choice=='P':
        page = customerFunc.preSearch(page, custlist)

    elif choice=='N':
        page = customerFunc.nextSearch(page, custlist)

    elif choice=='U':
        customerFunc.updateData(custlist)
    
    elif choice=='D':
        customerFunc.deleteData(custlist)
    
    elif choice=='Q':
        quit()
    return page


while True:
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

    page = exe(choice, page)