# Simple Grocery Store System 🍎🛒

A lightweight, command-line interface (CLI) application written in Python to manage a grocery store inventory. This project demonstrates the implementation of **CRUD** (Create, Read, Update, Delete) operations using Python dictionaries.

## 📋 Features

* **Add New Items:** Input unique IDs, product names, prices, and stock quantities.
* **View Inventory:** specific formatted display of all items currently in the system.
* **Edit Items:** Update the name, price, and quantity of existing products.
* **Delete Items:** Remove products from the inventory by ID.
* **Menu-Driven Interface:** Simple loop allowing multiple operations until the user chooses to quit.

## 🛠️ Technical Details

* **Language:** Python 3.x
* **Data Structure:**
    * The inventory is stored in a **Dictionary**.
    * **Key:** Item ID (String)
    * **Value:** List `[Name, Price, Quantity]`
    * *Example:* `{'101': ['Apple', 0.50, 100]}`

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have Python installed. You can check by running:
    ```bash
    python --version
    ```
2.  **Save the File:** Save the code as `grocery_system.py` (or any name you prefer).
3.  **Execute:** Open your terminal or command prompt and run:
    ```bash
    python grocery_system.py
    ```

## 🎮 Usage Example

When you run the program, you will see the main menu:

```text
1. Add New Item
2. View All
3. Edit Item
4. Delete Item
5. Quit

Choose option (1-5): 1
Enter Item ID: 101
Product Name: Milk
Price: 2.50
Quantity: 50
Item added.
