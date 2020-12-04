def discounted(price, discount, max_discount=50, name=''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount >= 99:
        raise ValueError('Максимальная скидка не более 99%')
    if discount >= max_discount or 'iphone' in name.lower() or not name:
        return price   
    else: 
        return price - price * discount / 100