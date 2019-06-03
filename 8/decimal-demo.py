from decimal import Decimal

fres = 1.1 + 2.2
dres = Decimal('1.1') + Decimal('2.2')

print('fres =', fres)
print('dres =', dres)
print('dres == Decimal(\'3.3\'):', dres == Decimal('3.3'))
print('dres == fres:', dres == fres)
