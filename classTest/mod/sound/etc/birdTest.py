# 일부로 오류 발생시키기 : raise
# class Bird:
#     def fly(self):
#         raise NotImplementedError

# # b = Bird()
# # b.fly()

# class B(Bird):
#     def fly(self):
#         print("bird ")

# b1 = B()
# b1.fly()

# 자신만의 에러 만들기
# class MyError(Exception):
#     def __init__(self):
#         print("바보 안됨")

# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()


# say_nick("바보")


class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()

try:
    say_nick("바보")
except MyError as err:
    print(err)