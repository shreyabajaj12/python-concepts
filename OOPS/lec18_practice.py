class C2dVec:
    def __init__(self,i,j):
        self.icap =i
        self.jcap =j
    def __str__(self):
        return f"{self.icap}i +{self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap =k
    def __str__(self):
        return f"{self.icap}i +{self.jcap}j +{self.kcap}"   
V2d = C2dVec(1,2)
V3d = C3dVec(1,9,7)
print(V2d)
print(V3d)
