# VITYARTHI-PROJECT
# 🧮 Simple Python Calculator – Explained!

Welcome to my mini-project!  
I created a **Python-based command-line calculator** that performs basic arithmetic operations along with **natural logarithm computation**. Below is a full explanation of what my code does and how it works.

---

## 📌 Overview
This program allows users to perform:

- ➕ **Addition**
- ➖ **Subtraction**
- ✖️ **Multiplication**
- ➗ **Division** (with zero-division safety)
- 📈 **Natural Logarithm (ln)**

It runs continuously until the user quits by typing **q**.

---

## 🏗️ Functions Implemented

### 1️⃣ Addition
```python
def add(x,y):
    return x+y
```
Returns the sum of two numbers.

---

### 2️⃣ Subtraction
```python
def subtract(x,y):
    return x-y
```
Subtracts the second number from the first.

---

### 3️⃣ Multiplication
```python
def multiply(x,y):
    return x*y
```
Returns the product of two numbers.

---

### 4️⃣ Division (with zero-division protection)
```python
def divide(x,y):
    if y==0:
        return "ERROR!!!!! Division by zero."
    return x/y
```
Prevents the user from dividing by zero.

---

### 5️⃣ Natural Logarithm (ln)
```python
def natural_log(x):
    if x <= 0:
        raise ValueError("ERROR!!!!!! Logarithm is only defined for positive numbers.")
    return math.log(x)
```
Only allows logarithms of positive numbers.

---

## 🖥️ Main Program Flow

The `main()` function:

- Shows a menu of available operations  
- Takes and validates user input  
- Handles invalid inputs  
- Performs calculations  
- Continuously runs until the user enters **q**  

It includes:

✔️ Error handling for non-number input  
✔️ Error handling for invalid logarithm values  
✔️ Clear and friendly messages  

---

## 🔁 Loop System
The calculator uses a `while True:` loop so the user can perform multiple operations without restarting the program.

---

## 🚫 Error Handling
The program avoids:

- ❌ Crashing due to invalid numeric input  
- ❌ Crashing when attempting log of negative/zero  
- ❌ Division by zero  

---

## 🏁 Exit Option
To quit the calculator, simply type:

```
q
```

---

## 🎉 Conclusion
This project helped me practice:

- Writing mathematical functions  
- Error handling with exceptions  
- Input validation  
- Menu-driven CLI systems  
- Basic Python programming structure  
