class mat_rev:

    def __init__(self):
        self.n=int(input())
        self.mat=[]

        for _ in range(self.n):
            self.mat.append(input().split(","))


        if input()[0]=="r":
            self.row_rev()
        else:
            self.col_rev()

        print(self)



    def __str__(self):
        ret="\n"

        for i in range(self.n):
            ret+=",".join(self.mat[i])+"\n"

        return ret[:-1]



    def col_rev(self):
        for i in range(self.n):
            self.mat[i].reverse()


    def row_rev(self):
        self.mat.reverse()
    

m=mat_rev()