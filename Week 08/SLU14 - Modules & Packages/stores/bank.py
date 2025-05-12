class Account:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_account_info(self):
        return f"Account number: {self.account_number}, Balance: {self.balance}, Owner's name: {self.owner_name}"

def get_total_balance(account_list):
    total_balance = 0
    for account in account_list:
        total_balance += account.balance
    return total_balance

description = "This is a module named bank."

if __name__ == "__main__":
    account1 = Account("123456", 1000.0, "John Doe")
    account2 = Account("789012", 2000.0, "Jane Smith")

    print(account1.get_account_info())
    print(account2.get_account_info())

    account1.deposit(500.0)
    account2.withdraw(1000.0)

    print(account1.get_account_info())
    print(account2.get_account_info())

    account_list = [account1, account2]

    print(f"Total balance: {get_total_balance(account_list)}")

