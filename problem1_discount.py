purchase_amount = float(input("Enter purchase amount: $"))
membership_status = input("Are you a member? (yes or no): ").lower()

# Choose the discount based on membership and purchase amount.
if membership_status == "yes":
    if purchase_amount >= 100:
        discount = 15
    else:
        discount = 5
elif purchase_amount >= 150:
    discount = 10
else:
    discount = 0

final_price = purchase_amount * (1 - discount / 100)

print(f"Discount applied: {discount}%")
print(f"Final price: ${final_price:.2f}")