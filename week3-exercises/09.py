import json
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def notify(self):
        pass

class EmailNotification(Notification):
    def notify(self):
        print("Email Notification")

class SMSNotification(Notification):
    def notify(self):
        print("SMS Notification")

json_data = """[ {"type": "Email"}, {"type": "Sms"}
]"""
datas = json.loads(json_data)

for data in datas:
    if data["type"] == "email":
        obj = EmailNotification()
    else:
        obj = SMSNotification()

obj.notify()