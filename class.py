class data:
    name=input("Enter your name")
    age=int(input("Enter your age"))
    print("The name is ",name," and the age is ",age)
class vehicle:
    def __init__(self,maxspeed,milage):
        self.maxspeed=maxspeed
        self.milage=milage
        print("The top speed is ",maxspeed," and the milage is ",milage)
ve=vehicle(201,19)