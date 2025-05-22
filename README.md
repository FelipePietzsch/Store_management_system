# 🛍️ Store Management System (OOP Practice Project)

This is a **basic practice project** created to explore and understand the principles of **Object-Oriented Programming (OOP)** in Python.  
It is intentionally simple and serves as an **exercise in structuring and organizing code using OOP concepts**.

## 🧠 Project Purpose

The main goal of this project was to:

- Learn how to create and use **classes and objects**
- Understand **inheritance**, **encapsulation**, and **polymorphism**
- Practice separating logic into multiple **Python modules**

This is not a production-ready project – it’s a personal learning exercise.

## 📂 Project Structure

The project is split into several Python files, each representing a part of the system:

- `main_store.py`: Starts the program and sets up the store and UI.
- `product.py`: Contains product classes like `Product`, `NonStockedProduct`, and `LimitedProduct`.
- `store.py`: Defines the `Store` class for managing products and handling orders.
- `promotion.py`: Includes promotion classes such as `PercentDiscount`, `SecondHalfPrice`, and `ThirdOneFree`.
- `user_interface.py`: A simple command-line interface for interacting with the store.

## ⚙️ Features (for practice)

- **Product Management**: Create and manage different types of products.
- **Promotions**: Attach promotions to products to simulate discounts.
- **Order Handling**: Let users place orders via the terminal UI.
- **Display**: Show available products and calculate total quantities.

## ▶️ How to Use

1. **Initialize Products** in `main_store.py`
2. **Apply Promotions** manually in the code
3. **Run the Program** to interact with the store via the terminal
4. **See Output** of your product setup and orders

## 🛍️ Pre-Initialized Store (main_store.py)

In main_store.py, a store instance called best_buy is created and initialized with the following products:
```python
product_list = [
    Product("MacBook Air M2", price=1450, product_quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, product_quantity=500),
    Product("Google Pixel 7", price=500, product_quantity=250),
    NonStockedProduct("Microsoft_word_software", price=500),
    LimitedProduct("Shipping_fee", price=50, product_quantity=inf, maximum=1),
    NonStockedProduct("Microsoft 8 Licence", 300, promotion_class=twenty_percent_promotion),
    Product("Galaxy fold S", price=1200, product_quantity=230, promotion_class=second_half_price),
    Product("ReMarkable_2", price=250, product_quantity=1000, promotion_class=third_one_free)
]
```

### 📱 Product Overview

•	**Product**: A standard physical product with a fixed quantity and price. It can have a promotion.  
•	**NonStockedProduct**: Represents virtual or digital products (like software). Their quantity is set to infinite and cannot be changed.  
•	**LimitedProduct**: A product that can only be bought a limited number of times per purchase, defined by the maximum parameter.  

### 🎁 Promotion Types

Promotions are implemented as classes that inherit from an abstract Promotion base class. Each promotion alters the final price calculation during a purchase.

1. **PercentDiscount**  
	•	Usage: twenty_percent_promotion.  
	•	Description: Reduces the price by a given percentage.  
	•	Example: If price is 300 and promotion is 20%, final price becomes 240.  

2. **SecondHalfPrice**  
	•	Usage: second_half_price.  
	•	Description: Every second item in a purchase is 50% off.  
	•	Example: Buying 2 items: First = full price, Second = 50% off.  

3. **ThirdOneFree**  
	•	Usage: third_one_free  .
	•	Description: For every 3 items, the third one is free.  
	•	Example: Buying 3 items = pay for 2, get 1 free.  

## 📌 Notes

- Products and promotions are **hardcoded** for now.
- No persistent storage – everything resets when you restart the script.
- The interface is **console-based** and minimal.

## 💡 Possible Improvements (for future practice)

- Allow **adding products dynamically** during runtime
- Implement **file-based or database storage** for persistence
- Add **error handling and input validation** to improve robustness

## 📚 License

This project is open for educational purposes and licensed under the MIT License.
