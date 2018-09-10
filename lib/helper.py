import random
import datetime

def FindInDict(tkey,dict_,rand=0):
	matches = []
	for key in dict_:
		if tkey == key:
			return key

	for key in dict_:
		if key in tkey:
			matches.append(key)
	if rand != 0:
		return matches[random.randint(0,len(matches)-1)]
	return matches



def logger(out):
	outtext= "[{}] {}".format(datetime.datetime.now(),out)
	print outtext
