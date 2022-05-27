# Don't forget to run your tests!

def is_character_match(string1, string2):
	# Your code here
	res = True 
	string1 = string1.lower()
	string2 = string2.lower()
	for i in string1:
		if i in string2:
			res = True
		else: return False
	return res
			


# print(is_character_match('charm', 'march'))