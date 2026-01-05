inventory = {
    "Laptop": {"price": 60000, "stock": 5},
    "Mouse": {"price": 500, "stock": 50},
    "Keyboard": {"price": 1500, "stock": 20}
}

def sell_product(inventory, product, quantity):
    if product not in inventory:
        return "Product not found"
    
    stock = inventory[product]["stock"]
    
    if stock < quantity:
        return "Insufficient stock"
    
    inventory[product]["stock"] = stock - quantity
    return "Product sold successfully"

def total_inventory_value(inventory):
    total = 0
    
    for item in inventory:
        price = inventory[item]["price"]
        stock = inventory[item]["stock"]
        total = total + (price * stock)
    
    return total

def low_stock_items(inventory):
    result = []
    
    for item in inventory:
        if inventory[item]["stock"] < 10:
            result.append(item)
    
    return result


def Analyse(inventory):
    answer = {}
    
    for item in inventory:
        price = inventory[item]["price"]
        stock = inventory[item]["stock"]
        
        answer[item] = {
            "price": price,
            "stock": stock
        }
    
    return answer

print(sell_product(inventory, "Mouse", 10))
print(sell_product(inventory, "Laptop", 3))
print(sell_product(inventory, "Laptop", 5))  

print("\nInventory Status:")
print(Analyse(inventory))

print("\nTotal Inventory Value:")
print(total_inventory_value(inventory))

print("\nLow Stock Items:")
print(low_stock_items(inventory))
