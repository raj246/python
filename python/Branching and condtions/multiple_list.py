in_stock = ['blue pens', 'papers', 'staples']

shopping_cart = ['blue pens', 'papers', 'staples', 'orange post-its']

for items in shopping_cart:
    if items in in_stock:
        print("Adding" + items + "to your order.")
    else:
        print("sorry" + items + " is not available.")
print("Your order is complete.")