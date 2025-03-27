# Calculate the final price after applying a discount.
    
#     Parameters:
#     price: The original price of the item.
#     discount_percent: The discount percentage.
    
#     Returns:
#     The final price after applying the discount if applicable.
def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price