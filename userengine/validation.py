import re
def validate(test_string):
	match = re.match("^[0-9a-zA-Z]{1,50}$", test_string)
	if match is not None:
		return True
	else:
		return False
