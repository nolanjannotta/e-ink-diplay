from datetime import datetime

raw_time = datetime.now().time()
time = raw_time.strftime("%I:%M %p")

print(time)