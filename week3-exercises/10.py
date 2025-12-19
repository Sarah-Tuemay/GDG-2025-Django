import json
from abc import ABC, abstractmethod
class Account(ABC):
    @abstractmethod
    def get_account_type(self):
        pass
class SavingAccount(Account):
    def get_account_type(self):
        print("Saving accoount")

class CurrentAccount(Account):
    def get_account_type(self):
        print("Current account")

accounts = """[
{"type": "saving"},
{"type": "current"},
]
"""

accountTypes = json.loads(accounts)
print(accountTypes)

