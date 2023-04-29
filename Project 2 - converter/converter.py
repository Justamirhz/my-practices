


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

co = Converter()
print("what to what? \n (1) C to F\n (2) F to C:")


t = int(input(""))

if t == 1:
    print("give me your C:")
    c = input("")
    co.C_to_fahrenheit(int(c))

    
