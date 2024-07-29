class Number:
    def sum(self):    #sum is a fun which run ona method              #methods
        return self.a +self.b
    
num =Number()        #object instantiation
num.a=12
num.b=34
s=num.sum()
print(s)
 

class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

shreyApplication = RailwayForm()
shreyApplication.name ="Shreya"
shreyApplication.train="Rajdhani Express"
shreyApplication.printData()

class vlog:
    name= "travel vlog"
    roll=123
    def info(self):
        print(f"{self.name} has a roll{self.roll}")
shrey=vlog()
shrey.roll=345
shrey.vlog="digital"
shrey.info()
rose=vlog()
rose.name="digital"
rose.info()
