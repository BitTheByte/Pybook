"""
please move this example to the root directory

"""

from lib.session import *
from lib.parser  import *
from lib.engine  import *


fbsession = login("myemail@somewhere.com","Secret_Password123") # login with facebook


def hi(msg):
	print msg
	return "HELLO FROM FUNCTION"
"""
def custom(message):
	print message
	return message + " WOW!"
"""

myreplies = {
	"hi":"Hello from python!",
	"failReply":"Sorry i don't understand :(",
	"func_hello":hi
}

options = {
    "keysearch" :1, # find the closest key replies 
    "failReply" :0, # use a fail reply
    #"replyHook" :custom,  use a custom function to generate answers
}



StaticMessageHook(fbsession,options,myreplies)
