from abc import ABC, abstractmethod

# Receiver
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depósito de {amount} feito na conta {self.account_number}. Novo saldo: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Saque de {amount} feito na conta {self.account_number}. Novo saldo: {self.balance}")
        else:
            print(f"Saldo insuficiente na conta {self.account_number}")

# Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command
class DepositCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.deposit(self.amount)

# Invoker
class TransactionManager:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
        self._commands = []

# Client
if __name__ == "__main__":
    # Cria uma conta
    account = Account("12345")

    # Cria um comando de depósito
    deposit_command = DepositCommand(account, 100)

    # Cria um invocador e adiciona o comando
    transaction_manager = TransactionManager()
    transaction_manager.add_command(deposit_command)

    # Executa os comandos
    transaction_manager.execute_commands()
