class ip:
    def read_file(self):
        self.file=open("ipaddress.txt","r")

    def con_list(self):
        self.ip_ad=[i.split(".") for i in self.file][:-1]

    def cal_res(self):
        self.A=0
        self.B=0
        self.C=0
        self.D=0
        self.E=0
        for i in self.ip_ad:
            c=int(i[0],2)

            if c<128:
                self.A+=1
            
            elif c<192:
                self.B+=1

            elif c<224:
                self.C+=1

            elif c<240:
                self.D+=1
            
            else:
                self.E+=1

    def print_res(self):
        print("A =",self.A)
        print("B =",self.B)
        print("C =",self.C)
        print("D =",self.D)
        print("E =",self.E)



obj=ip()
obj.read_file()
obj.con_list()
obj.cal_res()
obj.print_res()