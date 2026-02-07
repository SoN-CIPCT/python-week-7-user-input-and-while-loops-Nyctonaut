
# homework8_joshua_erlandsen.py
# Track pizza orders and confirm when completed.

# List of pizza orders
pizza_orders = [
    "Pepperoni",
    "Margherita",
    "Hawaiian",
    "Veggie",
    "Meat Lovers"
]

# Empty list for finished pizzas
finished_pizzas = []

# Process each order
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print("Your pizza pie is finished!")
    finished_pizzas.append(current_pizza)

# Print confirmation of completed orders
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")
