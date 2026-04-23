import numpy as np

sales = np.array([
    [120, 135, 150, 160],
    [90, 100, 110, 130],
    [140, 145, 155, 170],
], dtype=float)

product_names = np.array(["Keyboard", "Mouse", "Monitor"])

monthly_totals = sales.sum(axis=0)
product_totals = sales.sum(axis=1)
product_means = sales.mean(axis=1)
best_product_index = int(np.argmax(product_totals))

print("Monthly totals:", monthly_totals)
print("Product totals:")
for name, total, avg in zip(product_names, product_totals, product_means):
    print(f"- {name}: total={total:.0f}, avg={avg:.1f}")

print("Best product:", product_names[best_product_index])

high_sales_mask = sales >= 150
print("High-sales mask (>= 150):")
print(high_sales_mask)
print("Number of high-sales entries:", int(high_sales_mask.sum()))
