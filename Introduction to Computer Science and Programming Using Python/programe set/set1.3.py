def item_order(order):
    salad = 0
    hamburger = 0
    water = 0
    strs = []
    strs = order.split(' ')
    print str(strs)
    for i in strs:
        print i
        if i == 'salad':
            salad += 1
        elif i == 'hamburger':
            hamburger += 1
        elif i == 'water':
            water += 1
    
    print ('salad:[# %s] hamburger:[# %s] water:[# %s]') % (str(salad), str(hamburger), str(water))
    
order = raw_input('input your order: ')
item_order(order)