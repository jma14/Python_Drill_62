from datetime import *

currentTimeUTC = datetime.utcnow()
londonTime = currentTimeUTC
portlandTime = currentTimeUTC + timedelta(hours=-8)
newYorkTime = currentTimeUTC + timedelta(hours=-5)

portlandHour = portlandTime.hour
londonHour = londonTime.hour
newYorkHour = newYorkTime.hour

openTime = 9
closeTime = 21

if londonHour >= openTime and londonHour < closeTime:
    print 'The London branch is currently open'
else:
    print 'The London branch is currently closed'

if newYorkHour >= openTime and newYorkHour < closeTime:
    print 'The New York branch is currently open'
else:
    print 'The New York branch is currently closed'
