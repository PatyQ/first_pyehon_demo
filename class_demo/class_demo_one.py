class Dog:

    def __init__(self, name, color, variety):
        self.name = name
        self.color = color
        self.variety = variety  # 品种

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


