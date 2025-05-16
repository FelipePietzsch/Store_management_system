# Store Management System

This project is a simple store management system that allows you to manage products, take orders, and display the total quantity of all products. The system supports different product and promotion types.

## Project Structure

The project consists of the following Python files:

- `main_store.py`: Contains the main logic of the program, initializes the products, and starts the user interface.
- `product.py`: Defines different product classes such as `Product`, `NonStockedProduct`, and `LimitedProduct`.
- `store.py`: Contains the `Store` class that manages the products and processes orders.
- `promotion.py`: Defines various promotion types such as `PercentDiscount`, `SecondHalfPrice`, and `ThirdOneFree`.
- `user_interface.py`: Provides a user interface to interact with the store.

## Features

- **Product Management**: Add various types of products, including standard products, non-stocked products, and limited products.
- **Promotions**: Apply different promotions to products, such as percentage discounts, "second item half price," and "third item free."
- **Orders**: Take orders from users and process them.
- **Display**: Show all active products and the total quantity of products in the store.

## Usage

1. **Add Products**: Create instances of different product classes and add them to the store.
2. **Apply Promotions**: Apply promotions to products to create special offers.
3. **Take Orders**: Use the user interface to take orders from users.
4. **Display Products**: Display all active products and their details.

## Example

An example of initializing the store and using the user interface can be found in the `main_store.py` file.

## License

This project is licensed under the MIT License.

## Possible Add-ons

- **Dynamic Product Addition**: Currently, products can only be created during the initialization of the `Store` class. An enhancement could allow adding products dynamically during runtime.
- **Persistent Storage**: Products are currently only stored in memory during runtime. Implementing local storage, such as JSON or a database, could allow for persistent storage of products between sessions.
