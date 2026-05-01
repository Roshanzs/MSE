import databaseTool

def main():
    databaseTool.create_customer_database()
    databaseTool.create_transaction_database()
    databaseTool.create_account_database()
    databaseTool.create_bank_database()
    databaseTool.create_money_database()

if __name__ == "__main__":
    main()
