# App tells you when you will be a hundered years old

import time
name = raw_input("What's your name, fella? Go ahead, type it here: ")
age = int(raw_input("What's that age of yours, pal? Go ahead, let me know here: "))
curYear = time.localtime(time.time())
yearHundo = (100 - age) + int(curYear[0])
print ("Well, %s, it looks like you'll be 100 years old in the year %d." % (name, yearHundo))
