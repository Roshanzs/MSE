# Explanation and Necessity of Each Table

## table customers
This table stores basic customer information, including customer ID (id), name, email, phone, and age.
Necessity: It uniquely identifies and manages each customer, making it easy to associate with transactions, accounts, and other information.

## table transactions
This table records each transaction, including transaction ID (id), related customer (customer), bank name (bank_name), account (account), and transaction time (time).
Necessity: It tracks and manages all customer transaction records for easy query and auditing.

## table accounts
This table stores account information, including account ID (id), password, account type (type), balance, and unique account number (account_No).
Necessity: It manages customer account information, supports multiple accounts, and ensures account security.

## table banks
This table stores bank information, including bank ID (id), bank name (name), country, unique bank code (bank_code), and bank location (bank_location).
Necessity: It manages the list of supported banks, making it easy to associate bank information with accounts and transactions.

## table money
This table stores currency information, including currency code (currency_code), name, type, symbol, and value.
Necessity: It supports multi-currency management and currency exchange functions.