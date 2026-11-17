# Mini Project 2: Sales Data Analyzer using Lists and Dictionaries
# USN: 25BTRAD039

sales = []  # list of dictionaries: [{"name": ..., "qty": ..., "price": ...}]

while True:
    print("\n1. Add or Update Product Sales")
    print("2. Display Sales Summary & Total Revenue")
    print("3. Exit")
    
    ch = input("Enter choice (1-3): ").strip()

    if ch == "1":
        name = input("Enter product name: ").strip()
        if not name:
            print("Product name cannot be empty.")
            continue
        try:
            qty = int(input("Enter quantity sold: "))
            price = float(input("Enter unit price (Rs.): "))
            if qty < 0 or price < 0:
                print("Quantity and price must be non-negative.")
                continue
        except ValueError:
            print("Invalid numeric input for quantity or price.")
            continue

        # Check if product already exists to update it
        found = False
        for item in sales:
            if item["name"].lower() == name.lower():
                item["qty"] = qty
                item["price"] = price
                print(f"Product '{name}' record updated successfully.")
                found = True
                break
        
        if not found:
            sales.append({"name": name, "qty": qty, "price": price})
            print(f"Product '{name}' added successfully.")

    elif ch == "2":
        if not sales:
            print("No sales data available.")
            continue
        
        total_sales = 0
        top_product = sales[0]
        
        print("\n" + "=" * 65)
        print(f"{'Product Name':<15} | {'Quantity':<10} | {'Unit Price':<12} | {'Revenue (Rs)'}")
        print("-" * 65)
        
        for item in sales:
            rev = item["qty"] * item["price"]
            total_sales += rev
            if item["qty"] > top_product["qty"]:
                top_product = item
            print(f"{item['name']:<15} | {item['qty']:<10} | {item['price']:<12.2f} | {rev:<12.2f}")
            
        print("-" * 65)
        print(f"Total Overall Sales Revenue  : Rs. {total_sales:.2f}")
        print(f"Highest-Selling Product (Qty): {top_product['name']} ({top_product['qty']} units)")
        print("=" * 65)

    elif ch == "3":
        print("Exiting Sales Data Analyzer. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
