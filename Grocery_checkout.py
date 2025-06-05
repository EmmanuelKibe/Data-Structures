#items and their prices
items = {
    'apple': 30.0,
    'banana': 5.0,
    'orange': 10.0,
    'milk': 60,
    'bread': 65.0,
}

# Initialize an empty list to store the cart items
cart = []


def add_to_cart(item_name, quantity):
    """Add an item to the cart."""
    if item_name in items:
        item_price = items[item_name] * quantity
        cart.append({'name': item_name, 'quantity': quantity, 'price': item_price})
        print(f"Added {quantity} {item_name}(s) to the cart. Total price: {item_price:.2f}")
    else:
        print(f"Item '{item_name}' not found in the store.")

def total_price():
    """Calculate the total price of items in the cart."""
    total = sum(item['price'] for item in cart)
    return total


