toppings = ["chocolate", "strawberry sauce", "peanut butter"]
flavors = ["chocolate", "red velvet", "vegan", "normal"]
choice_sprinkles = ["with", "without"]


def greet():
    print("Hello! Welcome to Carolineas Donuts, what is your order?")


def show_flavors():
    # tem que mostrar por exemplo "1 - opção"
    for index, flavor in enumerate(flavors):
        print(str(index) + " - " + flavor)


def show_toppings():
    # também mostra exemplos de opções "1 - opção"
    for index, topping in enumerate(toppings):
        print(str(index) + " - " + topping)


def prompt():
    print("We have several options of flavors, sizes, toppings, with or without sprinkles and you choose the quantity too.\n")
    # variavel = expressao_de_func
    flavor = prompt_flavor()

    print("\nRight! And what topping would you want? \n")

    topping = prompt_topping()

    size = prompt_size()

    print("Great!")

    sprinkles = prompt_sprinkles()

    print("Okay!")

    quantity = prompt_quantity()

    print("Perfect. Your order is ready!")

    return [flavor, topping, size, sprinkles, quantity]


def prompt_quantity():

    quantity = ''
    while True:
        quantity = input(
            "\nAnd lastly, how many units would you like for this donut? (You can order up to 50 un). ")

        if validate_quantity(quantity):
            break

        print("Sorry but we do not have this quantity in stock today.")

    return quantity


def prompt_sprinkles():

    sprinkles = ''
    while True:
        sprinkles = input("\nWould you like it with or without sprinkles?  ")

        if validate_sprinkles(sprinkles):
            break

        print("Invalid option.")

    return sprinkles


def prompt_size():
    print("\nNow we can choose the size, it varies from 10 to 30 cm.")

    size = ''
    while True:
        size = input("\nHow many centimeters would be the size of your donut? ")

        if validate_size(size):
            break

        print("Could you please report the size of your donut correctly again please? ")

    return size


def prompt_topping():
    show_toppings()

    topping = ''
    while True:
        topping = input("\nEnter the flavor of the topping: ")

        if validate_topping(topping):
            break

        print("Sorry but we still do not have this flavor of topping.")

    return topping


def prompt_flavor():
    show_flavors()

    flavor = ''
    while True:
        flavor = input("\nWhat is the taste of dough? ")

        if validate_flavor(flavor):
            break

        print("Sorry but this dough taste we do not have in store.")

    return flavor


def validate_flavor(flavor: str):
    if flavor.lower() in flavors:
        return True

    if flavor.isdigit() and len(flavors) > int(flavor):
        return True

    return False


def validate_size(size: str):
    if not size.isdigit():
        return False

    siz = int(size)

    if siz < 10:
        print("Sorry, but the size should be larger than 10cm!")
        return False

    if siz > 30:
        print("Sorry, but the size should be less than 30 cm!")
        return False

    return True


def validate_topping(topping):
    if topping.lower() in toppings:
        return True

    if topping.isdigit() and len(toppings) > int(topping):
        return True

    return False


def validate_sprinkles(sprinkles: str):
    if sprinkles.lower() in choice_sprinkles:
        return True

    return False


def validate_quantity(quantity):
    if not quantity.isdigit():
        return False

    qnt = int(quantity)

    if qnt >= 50:
        return False

    return True


def show_result(order):
    flavor = order[0]
    if flavor.isdigit():
      flavor = flavors[int(flavor)]
    topping = order[1]
    if topping.isdigit():
      topping = toppings[int(topping)]
    size = order[2]
    sprinkles = order[3]
    quantity = order[4]

    print(
        f"Your {quantity} units of {flavor} donut with {topping} topping of {size} cm, {sprinkles} sprinkles!")
    print("Thank you for your order and come back!")


def main():
    greet()
    order = prompt()
    show_result(order)


if __name__ == "__main__":
    main()
