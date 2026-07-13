from data_loader import load_recommendation_data

orders, order_items, _, _ = load_recommendation_data()

orders = orders[orders["order_status"] == "delivered"]

interactions = orders.merge(order_items, on="order_id")

print("Delivered orders:", len(orders))
print("Order items:", len(interactions))

order_sizes = interactions.groupby("order_id").size()

print("\nOrders with more than one product:")
print((order_sizes > 1).sum())

print("\nMaximum products in one order:")
print(order_sizes.max())

print("\nAverage products per order:")
print(order_sizes.mean())