
def dragon_me(string):
	a = string

	b_1 = a[::-1]
	b_2 = b_1.replace("0", "x").replace("1", "y")
	b = b_2.replace("x", "1").replace("y","0")

	return "%s%s%s" % (a, "0", b)

def checksum_me(string):
	checksum = ""
	for i in range(0,len(string),2):
		ind_0 = string[i]
		ind_1 = string[i+1]

		if ind_0 == ind_1:
			checksum = checksum + "1"
		else:
			checksum = checksum +  "0"

	return checksum

def main(data, length):

	while len(data) < length:
		data = dragon_me(data)


	data = data[:length]

	#rint data

	checksum = checksum_me(data)

	while len(checksum) %2 == 0:
		checksum = checksum_me(checksum)

	print checksum


if __name__ == "__main__":
   test_data = "10000"
   data = "10111011111001111"
   test_length = 20
   length = 35651584

   #main(test_data, test_length)
   main(data, length)