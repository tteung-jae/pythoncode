# 클래스 명은 첫글자는 대문자로
# class Cookie:
#     pass

# a = Cookie()

# print(type(a))

# 사칙연산 클래스 만들기
# 모든 함수의 첫번째 인자는 self,
# self는 선언만 하고 사용자가 직접 사용하지 않는다.
# self.으로 붙은거는 class안에서만 사용
class FourCal:
    mode = 1

    def __init__(self, first=1, second=4):
        self.first = first
        self.second = second
        print("생성자")

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self. second
        return result

a = FourCal(2)
b = FourCal(4, 7)
c = FourCal()

a.setdata(3, 6)
b.setdata(3, 6)

print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))


FourCal.mode = 11
print()
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))

a.mode = 10
print()
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))
