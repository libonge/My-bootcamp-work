#  a list called menu with four items
menu = ['burger','pizza','pie','sandwich']

#  a dictonary called stock,containing the stock value
stock = {
    'burgers': 120,
    'pies': 110,
    'pizzas': 100,
    'sandwiches':150
}
# a dictionary called price,containing prices for each item
prices = { 
    'burgers': 30,
    'pies': 25,
    'pizzas': 50,
    'sandwiches':15
}
# calculation of the total stock worth in the cafe
total_stock = {key: stock[key] * prices[key] for key in stock}

print(total_stock)


print(sum(total_stock.values())) 
