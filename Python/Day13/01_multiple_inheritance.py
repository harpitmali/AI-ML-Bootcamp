class Father:
    def skill(self):
        print("Father: I know Trading")

class Mother:
    def cooking(self):
        print("Mother: I know Cooking")

class Child(Father, Mother):
    def hobby(self):
        print("Child: I love playing Football")

child = Child()

child.skill()
child.cooking()
child.hobby()