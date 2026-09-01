## Q2 PART 1
# These variables are defined for you to use.
MEMBER_DISCOUNT_RATE = 0.10
SALE_ITEM_DISCOUNT_RATE = 0.05

# This function is for you to implement!
def calculate_price(orig_price, is_member, is_on_sale):
    
    # ################################################################################
    # Modify the code below to return the correct discounted price.
    discount_rate = 0
    if is_member:
        discount_rate += 0.1
    if is_on_sale:
        discount_rate += 0.05

    final_price = orig_price * (1 - discount_rate)
    
    return final_price  
    # ################################################################################

## Q2 PART 2
# Write your code below to prompt the user for the following information: 
# (1) The original price of the item. 
# (2) Whether the user is a member or not. 
# (3) Whether the item is on sale or not.:

original_price = float(input("What's the orifinal price of the item: $"))
is_member = input("Are you a member [yes|no]? ")
is_on_sale = input("Is the item on sale [yes|no]? ")
is_member = "yes" == is_member
is_on_sale = "yes" == is_on_sale
final_price = calculate_price(original_price, is_member, is_on_sale)
print(f"The final price of the item is ${final_price}")