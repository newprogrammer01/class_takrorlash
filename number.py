# create a class Number
class Number:
    def __init__(self,number):
        self.number=number
    def get_number(self):
        return self.number
    def is_even(self):
        if self.number%2==0:
            return True
        else:
            return False
    def is_odd(self):
        if self.number%2==1:
            return True
        else:
            return False


x=Number(number=20)
print(x.is_odd())
