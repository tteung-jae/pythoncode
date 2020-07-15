class FourCal:

    def __init__(self, first=1, second=4):
        self.first = first
        self.second = second
        print("생성자")

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

###################################################

class MoreFurCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

cal1 = MoreFurCal(5, 0)
cal2 = MoreFurCal(5, 6)

print(cal1.add())
print(cal2.add())
print(cal1.pow())
print(cal2.pow())

print(cal1.div())