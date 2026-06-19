def fun():
    pass

sqr = lambda n : n ** 2

print(f"type(sqr) = {type(sqr)}")
print(f"5^ 2 = {sqr(5)}")

sum = lambda n1, n2 : n1 + n2
diff = lambda n1, n2 : n1 - n2
product = lambda n1, n2 : n1 * n2
qoetient =  lambda n1, n2 : n1 / n2

print(f"10 + 20 = {sum(10, 20)}")
print(f"20 - 10 = {diff(20, 10)}")
print(f"10 * 20 = {product(10, 20)}")
print(f"20 / 10 = {qoetient(20, 10)}")