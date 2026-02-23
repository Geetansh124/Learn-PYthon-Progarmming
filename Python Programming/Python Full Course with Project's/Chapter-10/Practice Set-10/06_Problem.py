from random import randint
class Train:

    def __init__(harry, trainNo):
        harry.trainNo = trainNo
         
    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")

    def getStatus(harry,):
        print(f"The train {harry.trainNo} is running on time")

    
    def getFare(harry,  fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to} is {randint(222, 5555)}")



t = Train(12399)
t.book("Kanpur", "Delhi")
t.getStatus
t.getFare("Kanpur", "Delhi")