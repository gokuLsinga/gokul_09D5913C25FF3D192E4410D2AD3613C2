3.1
def linearSearhProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result = linearSearhProduct(products, target)
print(result)
