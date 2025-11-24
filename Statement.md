# 📄 Project Statement – Python Calculator

## 📝 Introduction
This project is a **menu-driven Python calculator** designed to perform basic mathematical operations directly through the command line. It aims to provide a simple, interactive, and user-friendly way to perform calculations without requiring any external libraries other than Python’s built-in `math` module.

---

## 🎯 Project Objective
The main objective of this project is to:

- Implement basic arithmetic operations using Python functions.
- Add a natural logarithm function with proper input validation.
- Practice exception handling to prevent runtime crashes.
- Create a continuous loop-based menu system for user interaction.

---

## 🔍 Problem Definition
Users often need a quick tool to perform basic mathematical operations. This project solves that need by providing a lightweight calculator that:

- Accepts user input
- Validates it
- Performs the selected operation
- Returns the result instantly

Additionally, it ensures that the user cannot perform invalid operations such as:

- Division by zero  
- Logarithm of non-positive numbers  
- Entering non-numeric data  

---

## 🧠 Scope of the Project
The calculator currently supports:

- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division  
- 📈 Natural Logarithm (ln)

The program:

- Handles errors gracefully  
- Provides meaningful messages  
- Runs continuously until the user quits  
- Uses modular functions for readability  

---

## 🏗️ Methodology
1. **Function Creation**  
   Separate functions (`add`, `subtract`, etc.) were built to handle each operation.

2. **Input Handling**  
   The program reads user choices and numeric inputs using `input()`.

3. **Validation & Error Handling**  
   - Invalid numeric entries trigger error messages.  
   - Division by zero is detected and safely handled.  
   - Logarithm function checks for positive input.

4. **Loop-based Menu System**  
   A `while True` loop ensures the user can perform multiple calculations until they choose to quit.

---

## 📌 Expected Output
The program displays:

- A menu of available operations  
- Prompts for user input  
- Results of the chosen calculation  
- Error messages for invalid operations  
- A thank-you message when exiting  

---

## 🏁 Conclusion
This project demonstrates the use of:

- Python functions  
- Control flow statements  
- Error handling with `try`/`except`  
- Mathematical operations  
- User-friendly CLI interaction  

It is a simple yet effective example of a basic Python project with practical real-world application.