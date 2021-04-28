# Model
count = 0


class Tech:
    def __init__(self, model, price, state):
        self.model = model
        self.price = price
        self.state = state

    def print_details(self):
        print("Это родительский класс")

    def saymodel(self):
        print("Это модель %s" % self.model)

    def sayprice(self):
        print("Эта техника стоит %d рублей" % self.price)


class Notebook(Tech):
    def __init__(self, model, price, state):
        self.model = model
        self.price = price
        self.state = state


class Monitor(Tech):
    def __init__(self, model, price, state):
        self.model = model
        self.price = price
        self.state = state


class Printer(Tech):
    def __init__(self, model, price, state):
        self.model = model
        self.price = price
        self.state = state


class Microwave(Tech):
    def __init__(self, model, price, state):
        self.model = model
        self.price = price
        self.state = state


class TV(Tech):
    def __init__(self, model, price, state):
        self.model = model
        self.price = price
        self.state = state


class Buyer:
    def __init__(self, name, summ):
        self.name = name
        self.summ = summ

    def sayname(self):
        print("Здравствуйте, меня зовут %s" % self.name)

    def howmuch(self):
        print("У меня %d рублей" % self.summ)


class Proletarian:
    def __init__(self, name, post, salary):
        self.name = name
        self.post = post
        self.salary = salary

    def print_details(self):
        print("Это родительский метод из класса Proletarian")

    def sayname(self):
        print("Здравствуйте, я являюсь %s этого магазина, меня зовут %s" % (self.post, self.name))


class Cashier(Proletarian):
    def __init__(self, name, post, salary):
        self.name = name
        self.post = post
        self.salary = salary
        self.count = 0

    def countit(self):
        self.count += 1


class Manager(Proletarian):

    def __init__(self, name, post, salary):
        self.name = name
        self.post = post
        self.salary = salary
        self.count = 0

    def countit(self):
        self.count += 1

    # def talk(self):
    #   print("я могу предложить вам модель")
    #  print(Microwave.model)


Man_1 = Manager("Пётр", "Старший менеджер", 20000)
Mic_1 = Microwave("nt2", 1000, 1)
Boo_1 = Notebook("YokMakarek", 31000, 0)
Buy_1 = Buyer("Женя", 30000)
Cas_1 = Cashier("Мария", "Младший кассир", 10000)

Man_1.sayname()
Buy_1.sayname()
Buy_1.howmuch()
Boo_1.saymodel()
Boo_1.sayprice()

if Boo_1.price > Buy_1.summ:
    print("У меня недостаточно денег")
else:
    print("А насколько надежен этот аппарат?")

Mic_1.saymodel()
Mic_1.sayprice()

if Mic_1.price > Buy_1.summ:
    print("У меня недостаточно денег")
else:
    print("А насколько надежен этот аппарат?")

if Mic_1.state == 1:
    print("Эта техника надежна")
    print()
    print("Подскажите где находится касса?")
else:
    print("Эта техника ненадежна, не рекомендую")

Man_1.countit()
print("Я уже продал сегодня %d товаров" % Man_1.count)

Cas_1.sayname()
print("С вас %d рублей" % Mic_1.price)
Buy_1.summ -= Mic_1.price
Buy_1.howmuch()
Cas_1.countit()
print("Я уже продал сегодня %d товаров" % Cas_1.count)
