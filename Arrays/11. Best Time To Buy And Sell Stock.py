prices = [3, 8, 2, 5]
minimum_price =  prices[0]
maximum_profit = 0
for i in prices:
    if i < minimum_price :
        minimum_price = i
    if i - minimum_price > maximum_profit :
        maximum = i - minimum_price    
print("Maximum Profit :", maximum_profit )
print("Minimum :", minimum_price)