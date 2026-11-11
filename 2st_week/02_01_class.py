
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('hello, I am person', self.name, self.age)

    def talk(self):
        print("안녕하세요, 저는", self.name, "입니다.")

person1 = Person("홍길동", 22)
person1.talk()

person2 = Person("이순신", 45)
print(person2)



