# Lists of items and categories for slicing
items = "bubblegum, chocolate, pasta"
categories = "candy aisle, pasta aisle"
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[-5:]
category1 = categories[0:11]
category2 = categories[13:]
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
print("we have "+ candy1 + " for " + str(bubblegum_price) + " in the " + category1)
print("we have "+ candy2 + " for " + str(chocolate_price) + " in the " + category1)
print("we have "+ dry_goods + " for " + str(pasta_price) + " in the " + category2)