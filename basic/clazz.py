class Product:
    clazz_field=['class','field']
    def __init__(self):
        self.title="python"
        self.price=2000.0
    def to_s(self):
        return "title: {0}\nprice: {1}".format(self.title,self.price)


product = Product()
print(product)
product.remark="shit"
print(product.remark)

print product.clazz_field
print Product.clazz_field
print product.to_s()