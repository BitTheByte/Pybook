"""
please move this example to the root directory

"""

from lib.session import *
from lib.parser  import *
from lib.engine  import *


fbsession = login("myemail@somewhere.com","Secret_Password123") # login with facebook
mytext  = "Hello from python!" 
BasicMessageHook(fbsession,mytext)