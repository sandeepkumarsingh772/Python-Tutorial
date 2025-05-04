from random import randint

class Train:
    def __init__(slf, trianNo):
        slf.trianNo = trianNo

    def book(sandeep, fro, to):
        print(f"Ticket is booked in train no: {sandeep.trianNo} form {fro} to {to}") 
    
    def getstatus(self):
        print(f"Train no: {self.trianNo} is running on time")
    
    def getfare(self, fro, to):
        print(f"Train fare in train no: {self.trianNo} Form {fro} to {to} is {randint(222, 5555)}")

t = Train(23553)
t.book("Rampur", "CPR")
t.getstatus()
t.getfare("Rampur", "CPR")