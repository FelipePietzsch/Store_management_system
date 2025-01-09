import product
import store
import menu

def start(store):
    UI = menu.User_Interface(store)
    menu_funtions = {1: UI.list_all_products(),
                     2: UI.total_amount(),
                     3: UI.create_order(),
                     4: UI.quit()}


    while True:
        try:
            user_input = int(input("Please choose a number: "))
            # noch einfügen, dass mann von 1 bis 4 wärhen kann
            menu_funtions[user_input]()
        except ValueError as e:
            print(e)
a

def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()