class Property:
    all_taxes = 0

    def __init__(self, worth, coeff=0):
        self.worth = worth
        self.coeff = coeff

    def tax(self):
        Property.all_taxes += self.worth / self.coeff
        return self.worth / self.coeff


class House(Property):
    def __init__(self, worth, coeff=1000):
        super().__init__(worth)
        self.coeff = coeff


class Car(Property):
    def __init__(self, worth, coeff=200):
        super().__init__(worth)
        self.coeff = coeff


class Garden(Property):
    def __init__(self, worth, coeff=500):
        super().__init__(worth)
        self.coeff = coeff


how_much_money = int(input('Сколько у вас денег: '))

apartments = House(7000000)
bmw = Car(1000000)
fazed = Garden(2000000)
print(apartments.tax())
print(bmw.tax())
print(fazed.tax())
if how_much_money > Property.all_taxes:
    print('Вам хватает денег на содержание имущества')
else:
    print(f'Продавай что-нибудь, нищеброд, тебе не хватает {Property.all_taxes - how_much_money}')
