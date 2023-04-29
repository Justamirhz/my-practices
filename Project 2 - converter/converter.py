


class  Converter():
    def C_to_fahrenheit(self,i):
        f = (i*9)/5 + 32
        print(f)

    def fahrenheit_to_C(self,i):
        f = (i-32) * 5 / 9
        return f
    def kilogram_to_pound(self,i):
        f = i * 2.205
        return f



class calulate(Converter):

    def get_from_user(self,ch):
        if ch == 1:
            c = float(input("c:"))
            print(self.C_to_fahrenheit(c))

     

t = int(input("which one?"))
s = calulate()
s.get_from_user(t)

    
        


            