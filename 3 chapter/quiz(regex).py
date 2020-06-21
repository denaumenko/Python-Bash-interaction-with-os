import re
def check_web_address(text):
  pattern = r"^[A-Za-z][_\-A-Za-z\.]*\.[A-Za-z]*$"
  result = re.search(pattern, text)
  return result

print(check_web_address("My_Favorite-Blog.US")) # True

import re
def check_time(text):
  pattern = r"[0-9]*:[0-9][1-9]*[am pm AM]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("6:02am"))
print(check_time("five o'clock")) # False