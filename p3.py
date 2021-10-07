class div_list:

    def __init__(self):
        self.lr,self.ur=int(input()),int(input())
        self.op()

    def mul(n,k):
        r=n%k
        if not r:
            return n
        return n+k-n%k

    def op(self):
        self.o3=range(div_list.mul(self.lr,3),self.ur+1,3)
        self.o4=range(div_list.mul(self.lr,5),self.ur+1,5)
        s1=set(self.o3)
        s2=set(self.o4)
        self.o2=s1.intersection(s2)
        self.o1=s1.union(s2)

    def print_list(self):
        print()
        print(list(self.o1))  
        print(list(self.o2))  
        print(list(self.o3))  
        print(list(self.o4))      

    

div=div_list()
div.print_list()