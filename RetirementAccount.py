class RetirementAccount:
    """
    Represents a retirement account that the user can deposit money to and withdraw money from.

    It is also able to calculate return on investment depending on desired rate of return and length of investment.
    """

    def __init__(self, account_id, balance):
        """Creates a bank account object with an account ID and balance"""
        self._account_ID = account_id
        self._balance = balance

    def get_account_id(self):
        """Returns the account ID"""
        return self._account_ID

    def set_account_id(self, new_id):
        """Sets the account ID to a new value"""
        self._account_ID = new_id

    def get_balance(self):
        """Returns the current balance."""
        return self._balance

    def deposit(self, amount):
        """Deposits the specified amount into the account"""
        self._balance += amount

    def withdraw(self, amount):
        """Withdraws the specified amount from the account"""
        self._balance -= amount

    def balance_is_negative(self):
        """Returns True if the balance is negative and returns False otherwise"""
        return self._balance < 0

    def investment_return(self, rate_of_return, years):
        for element in range(years):
            self._balance = self._balance * (1 + rate_of_return)
        return self._balance


arturo = RetirementAccount(100, 50000)
arturo.deposit(500000)
print(arturo.get_balance())
arturo.investment_return(.10, 10)
print(arturo.get_balance())
