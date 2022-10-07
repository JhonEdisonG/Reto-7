from code import interact


class person:
    def __init__(self,name,age,size,hair_color):
        self.name=name
        self.age=age
        self.size=size
        self.hair_color=hair_color
    def walk(self,distance):
        print(f"{self.name} esta caminando {distance} metros diarios")
    def eat(self,food):
        print(f"{self.name} esta comiendo {food}")
    def speak(self,language):
        print(f"{self.name} habla en {language}")

class student(person):
    def study(self,subject):
        print(f"{self.name} esta estudiando {subject}")
class teacher(person):
    def __init__(self, name, age, size, hair_color):
        super().__init__(name, age, size, hair_color)
    def teach(self,subject):
        print(f"{self.name} esta enseñando {subject}")
    
s1=student("Monica",18,1.57,"negro")
t1=teacher("Gildardo",30,1.70,"castaño")

s1.study("Calculo integral")
t1.teach("Calculo integral")
s1.eat("Ajiaco")
s1.walk(1000)
s1.speak("Italiano")