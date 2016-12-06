import md5

def main(input, is_test=False):

	password = [""]*8
	print password

	i = 0;
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

			#if hexa[5] in ["0", "1", "2", "3", "4", "5", "6", "7"]:
			pos = int(hexa[5], 16)
			if pos < 8 and password[pos] == "":
				password[int(hexa[5])] = hexa[6]

			print password

		i+=1

		if "" not in password:
			running = False

	print password
	if is_test:
		assert "".join(password) == "05ace8e3"

if __name__ == "__main__":
   test = "abc"
   real = "reyedfim"

   main(real)

