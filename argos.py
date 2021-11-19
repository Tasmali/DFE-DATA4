def stock_stuff(inputvar):
    productcodelen = len(inputvar)
    return productcodelen

product_code = input ("What do you wish to buy?")
returnvar = stock_stuff(product_code)
print("Your product code was", returnvar, "characters long" )