import sys
import re
from collections import OrderedDict

def main(arg):
	reals_int = []
	reals = {}

	reals_new_phrases = {}

	def is_real(line):
		checksum = line.split('[')[1].replace("]","").replace("\n", "")
		before_checksum = line.split('[')[0]

		print checksum

		before_checksume_sorted = ''.join(sorted(before_checksum))

		print before_checksume_sorted

		p = re.compile('\D+')
		chars = p.findall(before_checksume_sorted)[1]

		print chars

		most_commons = {}
		added_common_char = {}

		for char in chars:
			if char in added_common_char:
				continue

			if chars.count(char) in most_commons:
				most_commons[chars.count(char)] += char
			else:
				most_commons[chars.count(char)] = char

			added_common_char[char] = "added"

		print most_commons

		d_descending = OrderedDict(sorted(most_commons.items(),
                        key=lambda t: t[0], reverse=True))

		print d_descending

		checksum_should_be_list = []

		for x in range(0,len(d_descending)):
			checksum_should_be_list.append(d_descending.popitem(last=False)[1])

		checksum_should_be = "".join(checksum_should_be_list)[0:5]

		print "checksum_should_be"
		print checksum_should_be

		p = re.compile('\d+')
		val = p.findall(before_checksum)

		if val and checksum_should_be == checksum:
			reals[line] = int(val[0])
			return int(val[0])

	def new_letter(letter, shift):
		letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u" ,"v" ,"w" ,"x" ,"y" ,"z"]

		if letter == "-":
			return " "

		index = letters.index(letter)

		if index + shift >= len(letters):
			return letters[index+shift - len(letters)]
		else:
			return letters[index+shift]

	with open(arg) as f:
		for line in f:
			if line == "\n":
				break

			val = is_real(line)

			if val:
				reals_int.append(val)

			for real, number in reals.iteritems():
				words = real.replace(str(number), "")
				words = words.split("[")[0]

				new_words = ""

				shift = number % 26

				for letter in words:
					new_words += new_letter(letter, shift)

				reals_new_phrases[new_words] = number

	print sum(reals_int)

	for new_phrases, number in reals_new_phrases.iteritems():
		if "north" in new_phrases:
			print new_phrases
			print number

if __name__ == "__main__":
   main(sys.argv[1])
   #main2(sys.argv[1])