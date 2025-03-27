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

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
print(f"Final price after discount (if applicable): ${final_price:.2f}")



