# def tail_recursion(factorial, result = 1): #A function to find the factorial of a number using tail recursion
#     if factorial == 1:
#         return result
#     else:
#         temp_result = factorial * result
#         return tail_recursion((--factorial),temp_result)



# user_funds = 10.31
# item_price = input("Burger price: ")

# if item_price < user_funds:
#     print("You have enough money!")
# elif item_price == user_funds:
#     print("You have the precise amount of money")
# elif item_price < user_funds:
#     print("Sorry you don't have enough money")



# def product(n):
#      total = 1
#      for i in n:
#          total *=i
#      return (total)

# print(product([4,4,5]))


import pdb
pdb.set_trace()

def is_prime(x):
      if x < 2:
          return False
      else:
          for n in range(2, x-1):
              if x % n == 0:
                  return False
      return True



item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
        n= n+1

print (item_list[4])
      