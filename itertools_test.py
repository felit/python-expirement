# http://python.jobbole.com/85321/
# https://docs.python.org/2/library/itertools.html
# http://python.jobbole.com/87380/
from decimal import Decimal
from itertools import groupby

vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
            ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
            ('Dodge', 'Charger'), ('Ford', 'GT')]

sorted_vehicles = sorted(vehicles)

for key, group in groupby(sorted_vehicles, lambda make: make[0]):
    for make, model in group:
        print('{model} is made by {make}'.format(model=model,
                                                 make=make))
    print ("**** END OF GROUP ***n")
print Decimal('3.14')
# Decimal
print float(Decimal('3.14'))

params = {}
params['hello'], params['world'] = 1, 2
print params
