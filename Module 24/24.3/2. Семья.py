class SomeFamily:
    name = None
    money = 0
    having_house = False

    def home_sweet_home(self):
        if self.having_house:
            return 'имеется'
        else:
            return 'нет'

    def info(self):
        print(f'Название: {self.name}\n'
              f'Бюджет: {self.money}\n'
              f'Наличие дома: {self.home_sweet_home()}')

    def buy_a_house(self, house_price):
        while not self.having_house:
            if self.money > house_price:
                self.money -= house_price
                self.having_house = True
                print('Поздравляем с покупкой дома!\n'
                      f'Еще и осталось {self.money} денег!')
            else:
                print(f'Денег пока не хватает, нужно еще {house_price - self.money} денег')
                self.earn_money()

    def earn_money(self):
        some_money = int(input('Сколько денег заработала семья: '))
        self.money += some_money


smith = SomeFamily()
smith.name = 'Смиты'
smith.money = 100000
smith.info()
smith.buy_a_house(1000000)
