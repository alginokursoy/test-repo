import os
import sys


import requests


def say_something(sentences):
    for i in sentences.split(" "):
        os.system("say %s" % i)


r = requests.get("https://coreyms.com")
print(r.status_code)
name = input("Your Name?  ")
say_something("merhaba %s" % name)
print(sys.executable)

