def money_count(budjet, taxes):
    if budjet + taxes > budjet:
        print('Бюджет увеличился')
    else:
        print('Бюджет не изменился')


budget = float(input('Введите бюджет страны: '))
taxes = float(input('Введите сумму налогов: '))

money_count(budget, taxes)
