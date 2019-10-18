import uuid
import argparse

# https://pynative.com/python-generate-random-string/
def randomPassword(stringLength):
		randomString = uuid.uuid4().hex # get a random string in a UUID fromat
		randomString  = randomString.upper()[0:stringLength] # convert it in a uppercase letter and trim to your size.
		print(randomString)

if __name__ == '__main__':
	# setup our arguments - 1 or zero arguments
	parser = argparse.ArgumentParser(description="Enter a number to indicate length of password - default is 16")
	parser.add_argument("stringLength", nargs='?', default=16, const=1, type=int, help='Password Length')
	args = parser.parse_args()

	stringLength = args.stringLength

	randomPassword(stringLength)