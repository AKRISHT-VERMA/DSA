'''Mistake I Almost Made

I thought updating the minimum price later
meant the algorithm was changing the
buying day of the final answer.

Reality:

minimum_price is only used to compute
future profits.

maximum_profit already stores the best
transaction found earlier.

Updating minimum never erases a better
profit already discovered.'''

prices = [3, 8, 2, 5]
minimum_price =  prices[0]
maximum_profit = 0
for i in prices:
    if i < minimum_price :
        minimum_price = i
    if i - minimum_price > maximum_profit :
        maximum_profit = i - minimum_price    
print("Maximum Profit :", maximum_profit )
print("Minimum :", minimum_price)