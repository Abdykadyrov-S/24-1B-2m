"ООП - Объектно-Ориентированное Программирование"

# class MyHome(): # чертеж или же шаблон
#     win = 16 # атрибут класса
#     # self - сам объект
#     # self - ссылка на текущий объект
#     def __init__(self, door, color): # __init__ - конструктор
#         self.door = door # атрибут объекта
#         self.color = color # атрибут объекта
    
#     def info_about_home(self):
#         print(f"кол-во окон:{self.win}, цвет: {self.color}")
        

"home - объект"
"экземпляр класса"

# home = MyHome(4, "white") 
# home_2 = MyHome(8, "brown") 
# home.info_about_home()

# print(home.win)
# print(home.door)
# print(home.color)

# print(home_2.win)
# print(home_2.door)
# print(home_2.color)


# def my_home(a,b):
#     print("Hello world")

# my_home()

# num = int(54)
# list
# int
# print(type(num))


class Car():
    def __init__(self, marka, model, year, color, max_speed):
        self.marka = marka
        self.model = model
        self.year = year
        self.color = color
        self.is_start = False
        self.max_speed = max_speed
    
    def info(self):
        print(f"""марка-{self.marka} , модель- {self.model}, год- {self.year}, цвет- {self.color}""")
        print("Машина не заведена")

    def start(self):
        self.is_start = True
        print("Машина завелась")

    def drive(self, speed:int):
        if self.is_start == True:
            if speed < self.max_speed:
                print(f"Машина {self.marka}-{self.model} едет со скоростю {speed} км/ч")
            else:
                print(f"Машина {self.marka}-{self.model} не сможет набрать такую скорость")
        else:
            print("Пожалуйста заведите машину")

mers = Car("mersedes", "CLS", 2025, "Black", 340)
matiz = Car("daewoo", "matiz", 2006, "red", 200)
mers.info()
mers.start()
mers.drive(300)
matiz.start()
matiz.drive(300)
