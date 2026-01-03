# ATM Simulator

A simple **Python-based ATM simulator** that allows a user to:

* Check account balance
* Deposit money
* Withdraw money
* View transaction history
* Exit the ATM

The program includes **basic input validation** to prevent crashes from invalid inputs.



## Features

* **PIN verification** with 3 attempts limit
* **Balance tracking**
* **Transaction history** for deposits, withdrawals, and balance checks
* **Input validation** for numeric amounts and menu choices
* **Safe handling** of negative or zero deposits/withdrawals



## How to Use

1. Run the Python script:

   python atm.py

2. Enter your **account number** (for realism).
3. Enter the **account PIN** (`1234` by default).
4. Choose from the menu options by entering the corresponding number:

   * `1` → Check Balance
   * `2` → Deposit Money
   * `3` → Withdraw Money
   * `4` → Transaction History
   * `5` → Exit



## Requirements

* Python 3.x
* No external libraries required


## Notes

* All inputs are validated to prevent crashes
* Deposits and withdrawals must be **positive integers**
* Exceeding the withdrawal limit will prompt an **Insufficient balance** message

