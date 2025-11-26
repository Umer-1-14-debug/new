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
class birds:
    specie="bird"
    def __init__(self,name,type1):
        self.name=name
        self.age=type1
    def s(self):
        print(self.specie)
        print(self.name)
        print(self.type1)
bi1=birds("sparrow","b1")
bi2=birds("crow","b2")
bi1.s()
bi2.s()
