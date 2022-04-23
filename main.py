# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from class_demo.class_demo_one import Dog, Demo


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def for_demo():
    a = ["qax", "wsxa", "edc"]
    for v in a:
        print(v)
    print("a.count(a)", a.count("qax"))
    squares = [value * 2 for value in range(1, 11)]
    print(squares)
    sub_squares = squares[:3]
    print(sub_squares)


def demo_two(str, list):
    list = list.append(100)
    print(list)
    str = str + 10
    print(str)


def demo_six(*key, **key2):
    pass


def show():
    print("定义在类之外的函数")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    my_dog = Dog("豆豆", "黄色")  # 构造函数参数必须全填,不能为空
    # my_dog2 = Dog()
    Dog.roll_over(my_dog)
    my_dog.sit()
    my_dog.age = 3
    print(my_dog)
    # print(my_dog2)
    my_dog.show = show
    my_dog.show()
    Demo()
    print("--------------------------------")
    c = ''.join(["a", 'b', 'c', 'd'])
    s = 0
    l = [1, 2, 3]
    demo_two(s, l)
    print("s", s)
    print("s", l)
    print(c)
    for_demo()
    x = 1
    print(id(x))
    x = 2
    print(id(x))
    if x == 0:
        print(x)
    elif x == 1:
        print("haha" + "word")
    else:
        print("not" + "go")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


