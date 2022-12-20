import time
from datetime import datetime
from datetime import timedelta
ts = int('1527256802')

dt = datetime.utcfromtimestamp(ts).strftime('%y-%m-%d %H:%M:%S')
dt = datetime.strptime(dt,'%y-%m-%d %H:%M:%S')  + timedelta(hours=3)
print(dt)
ts = int(dt.timestamp())
print(ts)
