class Animal:
    variety = ""  # 品种

    def eat(self):
        print(f"{self.variety}吃饭")


class Dog(Animal):  # 继承

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


class Fish(Animal):
    def __init__(self, shape, size):
        self.shape = shape
        self.size = size

    def swim(self):
        print("鱼游泳")

    # 重写方法
    def eat(self):
        super().eat()  # 金鱼吃饭
        print(f"{self.variety}吃虾米")  # 金鱼吃虾米


def Demo():
    fish = Fish("oval", "BIG FISH")
    fish.variety = "金鱼"
    fish.eat()
