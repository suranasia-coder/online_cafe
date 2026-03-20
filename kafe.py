import os
os.system('cls')
menu={
'Cappuccino':80,
'Latte':40,
'Mocha':30,
'Cupcake':10 ,
'Ice tea':30, 
'Chips':10 ,
'Ice coffee':30,
'Salad': 50,
}

print('Welcome to Cloud Nine Café ' ) 
for items, price in menu.items():
    print(f'{items}:{price}kr ')

order= {}
while True:
    item= input('Enter the name of item you want to order: ').title()

    if item in menu:
        qty= int(input('Enter Quantity :'))
        order[item]= order.get(item,0) + qty
        print(f'Your item {qty}  {item} has been added to your order ')
    else:
        print(f'Ordered item {item} not found')
        print('Kindly order something that we have in the menu. ')

    any_order=input('Wanna order something more (y/n) ')
    if any_order=='n':
        break
    if any_order=="y":
        continue
print( '----Bill-----')
tot_bill=0
for items, price in order.items():
    item_total= menu[item]*qty
    tot_bill+= item_total
    print(f'{items} x {qty}= {item_total}')
print( f'The total amount of items to pay is {tot_bill} kr')
