import retail_utility

user_wants_to_spend = int(input("How much money do you want to spend? "))

price_1kg_jar = 98.50
price_500g_jar = 58.50

num_1kg_jars, change = retail_utility.calculate_max_quantity_and_change(price_1kg_jar,user_wants_to_spend)
num_500g_jars, change = retail_utility.calculate_max_quantity_and_change(price_500g_jar,change)
grams_of_honey = num_1kg_jars * 1000 + num_500g_jars * 500
print(f"You can buy {grams_of_honey} grams of honey. You have ${change} left as your change.")