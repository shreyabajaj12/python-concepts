class Train:
    def __init__(self,name,fare,seats) :
        self.name = name
        self.fare = fare
        self.seats =seats

    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats availabe in this train is{self.seats}")

    def fareInfo(self):
        print(f"The price of the tickets is :rs{self.fare}")

    def bookticket(self):
        if(self.seats>0):
            print(f"Your tickets has been booked your seat no is {self.seats}")
            self.seats=self.seats-1
        else:
            print("kindly try in tatkal")
    def cancelTickets(self, seatno):
        pass
intercity = Train("Intercity Express 14015",90,300)
intercity.getstatus()
intercity.fareInfo()
intercity.bookticket()
intercity.getstatus()        