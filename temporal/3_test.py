class Suma:
    def __init__(self,num_1=0,num_2=0):
        self.num_1 = num_1
        self.num_2 = num_2
    def suma(self,num_1,num_2):
        print(num_1+num_2)
    def resta(self,num_1,num_2):
        print(num_1-num_2)

n1 = 10
n2 = 25


s = Suma()
s.suma(n1,n2)
s.resta(n1,n2)