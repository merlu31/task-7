#creating file content with curent timestamp
# using time module
import time
# ts stores the time in seconds
ts = time.time()
# print the current timestamp
print(ts)
import datetime
time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 
print(time_now)
# import module
from datetime import datetime
# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print("Current date & time : ", current_datetime)
# convert datetime obj to string
str_current_datetime = str(current_datetime)
# create a text file object along with extension
file_name = str_current_datetime+".txt"
file = open(file_name, 'w')
print("File created : ", file.name)
file.close()