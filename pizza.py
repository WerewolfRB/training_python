def make_pizza(size, *toppings):
    print(f'Длина {size} состав: ')
    for topping in toppings:
        print(f'> {topping}')


