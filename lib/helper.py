import random
import datetime

def FindInDict(tkey,dict_,rand=0):
	for key in dict_:
		if tkey == key:
			return key
	matches = [key for key in dict_ if tkey.find(key) != -1]
	return matches[random.randint(0,len(matches)-1)] if rand != 0 else matches



def logger(out):
	outtext= "[{}] {}".format(datetime.datetime.now(),out)
	print outtext
