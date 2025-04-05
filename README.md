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

---

## 🧠 How the Program Works (Step-by-Step)

The logic in `main.py` follows these steps:

1. **Input**:  
   Prompts the user to enter two names.

2. **Preprocessing**:
   - Removes spaces and converts both names to lowercase for consistency.

3. **Letter Cancellation**:
   - Counts and cancels out common letters between the two names.
   - The remaining number of characters is used to determine the relationship.

4. **FLAMES Logic**:
   - Iteratively removes letters from the word "FLAMES" using the count of unmatched letters.
   - The process continues until only one letter remains.

5. **Result**:
   - The final letter corresponds to a relationship type, which is then displayed to the user.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x installed on your system.

### 📥 Installation

Clone the repository:

```bash
git clone https://github.com/psyccho00/FLAMES.git
cd FLAMES
