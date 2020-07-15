# FileNotFoundError
# f = open("./classTest/test.txt", "r")

# ZeroDivisionError
# 4/0

# IndexError
# li = [2, 3, 4]
# li[3]

# 오류가 발생했을시 메세지 뜨게하기
try:
    # 4/1
    4/0
    # f = open("./classTest/test.txt", "r")
    # li = [2, 3, 4]
    # li[3]
except IndexError as err:
    print(err)
except ZeroDivisionError as err:
    pass    # 에러가 나도 그냥 지나가게 함
except FileNotFoundError as err:
    print(err)
finally:    # 에러가 났든 안났든 무조건 실행
    print("finally")