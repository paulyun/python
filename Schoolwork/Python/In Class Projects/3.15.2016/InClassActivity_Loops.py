#"Consignment In-Class Assignment" "While loops"
original_price = float(input("Please input the Original Price of the item"))
months = 1
price = original_price

while (months<=3):
    owner_cut = (price * 0.6)
    store_cut = (price * 0.4)
    print("The final price of the sold item was", price)
    print("The Store received", format(store_cut, '.2f'))
    print("The Items owner received", format(owner_cut, '.2f'))
    item_sold = input("Did you sell the item? Enter Y for Yes and N for No")
    if (item_sold == 'Y' or item_sold == 'y'):
        if(months==1):
            print("The Item was sold in the month", months, "st month.")
            break
        elif(months==2):
            print("The Item was sold in the month", months, "st month.")
            break
        elif(months==3):
            print("The Item was sold in the month", months, "st month.")
            break
    else:
        price = (price * 0.8)
        months = months + 1
        continue
    
    
#"Consignment In-Class Assignment" "For loops"
original_price = float(input("Please input the Original Price of the item"))
months = 1
price = original_price

for months in range(1, 4):
    owner_cut = (price * 0.6)
    store_cut = (price * 0.4)
    print("The final price of the sold item was", price)
    print("The Store received", store_cut)
    print("The Items owner received", owner_cut)
    price = (price * 0.8)


#Extra loop codes    
original_price = float(input("Please input the Original Price of the item"))
months = 1
price = original_price

#while (months<=3):
for months in range(3):
    owner_cut = (price * 0.6)
    store_cut = (price * 0.4)
    print("The final price of the sold item was", price)
    print("The Store received", store_cut)
    print("The Items owner received", owner_cut)
    price = (price * 0.8)
    #months = months + 1