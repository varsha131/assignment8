Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def findLength(string):
    count=0
    for i in string:
        count+=1
    return count
string="refrigerator"
print(findLength(string))