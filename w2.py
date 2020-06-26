Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def remove(string,i):
    for j in range(len(string)):
        if j==i:
            string=string.replace(string[i], " ",1)
    return string
if__name__ == '__main__':
    string="python program"
    i=5
    print(remove(string,i))