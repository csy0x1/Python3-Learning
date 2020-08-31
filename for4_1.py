pizzas=['1','2','3','4','5','6']
print('first three:')
print(pizzas[0:3])
print('\nthe middle three')
print(pizzas[2:5])
print('\nthe last three')
print(pizzas[-3:])

friends_pizza=pizzas[:]
pizzas.append('7')
friends_pizza.append('8')
print('my:')
for pizza in pizzas:
    print(pizza)
print('friends')
for pizza in friends_pizza:
    print(pizza)