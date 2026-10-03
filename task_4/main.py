def main():

    items = [
        ("apple", "fruit"),
        ("banana", "fruit"),
        ("carrot", "vegetable"),
        ("tomato", "vegetable"),
        ("milk", "dairy")
    ]

    products = dict()

    for element in items:
        if element[1] not in products:
            products[element[1]] = []

    for product in items:
        if product[1] in products:
            products[product[1]].append(product[0])

    print(products)


if __name__ == "__main__":
    main()
