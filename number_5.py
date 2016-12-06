import md5

def main(input, is_test=False):

	password = ""

	i = 1;
	running = True

	key = '00000'
	while running:

		tried = "%s%s" % (input, str(i))
		m = md5.new(tried)
		hexa = m.hexdigest()

		if key in hexa[0:5]:
			print tried
			print i
			print hexa
			password = "%s%s" % (password, hexa[5])

		i+=1

		if len(password) == 8:
			running = False

	print password
	if is_test:
		assert password == "18f47a30"

if __name__ == "__main__":
   test = "abc"
   real = "reyedfim"

   main(real)

