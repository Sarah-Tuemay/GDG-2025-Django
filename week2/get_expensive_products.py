prices = [120, 45, 300, 85, 150]

def get_expensive_products(prices):
    expensive_products = []
    for num in prices:
        if num > 100:
            expensive_products.append(num)
    
    return expensive_products

print(get_expensive_products(prices))
