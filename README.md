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

## 🔍 Example

Example usage is shown in `main_store.py`.  
It demonstrates how to create products, assign promotions, and start the store interface.

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
