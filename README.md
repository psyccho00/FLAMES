# 🔥 FLAMES - Relationship Compatibility Game

**FLAMES** is a classic compatibility game that determines the relationship between two people based on their names. Whether you're curious about love, friendship, or rivalry, this game is a fun way to find out!

---

## 📜 What Does FLAMES Stand For?

- **F** - Friends
- **L** - Love
- **A** - Affection
- **M** - Marriage
- **E** - Enemies
- **S** - Siblings



## 🧠 Step-by-Step How the Code Works

The script in `main.py` follows these key steps:

### 1. 📥 Input Collection
- The program prompts the user to enter two names.

### 2. ✨ Preprocessing
- Converts both names to lowercase.
- Removes all whitespace to ensure fair character comparison.

### 3. 🔠 Unique Letter Count
- Compares both names.
- Cancels out matching letters from both.
- Counts the number of non-common characters.

### 4. 🔁 FLAMES Elimination Process
- Creates a list from the string `"FLAMES"`.
- Uses the count from the previous step to eliminate letters cyclically.
- Repeats until one letter remains.

### 5. 🧩 Match Result
- The last remaining letter is mapped to a relationship:
  - **F** = Friends
  - **L** = Love
  - **A** = Affection
  - **M** = Marriage
  - **E** = Enemies
  - **S** = Siblings

### 6. 🎉 Display Result
- Outputs the relationship result based on the FLAMES logic.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x installed on your system.

### 📥 Installation

Clone the repository:

```bash
git clone https://github.com/psyccho00/FLAMES.git
cd FLAMES
```
Clone the repository:

```bash
git clone https://github.com/psyccho00/FLAMES.git
cd FLAMES
```
