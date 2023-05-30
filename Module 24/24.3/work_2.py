class Family():
    surname = 'Common Family'
    money = 100000
    have_a_house = False

    def info(self):
        print(
            f'Family name: {self.surname}\n'
            f'Family founds: {self.money}\n'
            f'Family house: {self.have_a_house}'
        )

    def earn_money(self, amount):
        self.money += amount
        print(f'Заработал {amount} денег. Теперь денег {self.money}')

    def buy_house(self, house_price, discoutn=0):
        house_price -= house_price * discoutn / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print(f'Поздравляем, дом куплен и осталось {self.money} денег')
        else:
            print(f'Не хватает {house_price - self.money} денег')


smith = Family()
smith.info()
smith.buy_house(1000000)
if not smith.have_a_house:
    smith.earn_money(9000000)
    smith.buy_house(10000000, 10)
print(smith.info())
