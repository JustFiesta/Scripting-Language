from datetime import datetime

usrDate = input("Podaj datę (rrrr-mm-dd): ")

usrDate = datetime.fromisoformat(usrDate)
now = datetime.today()

print(usrDate - now)