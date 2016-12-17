import sys

def main(arg, expected=None):
  total = 0

  with open(arg) as f:
    for line_index, line in enumerate(f):
      print line

      line = line.replace("\n", "")

      cursor = 0
      result = ''

      for i, char in enumerate(line):
        if i < cursor:
          continue

        if char == '(':
          x_pos = line[cursor:].find('x') + cursor
          number = int(line[cursor + 1 : x_pos])
          end_par_pos = line[x_pos:].find(')') + x_pos
          repeat = int(line[x_pos + 1 : end_par_pos])

          decomp = line[end_par_pos+1 : end_par_pos + number + 1]
          for j in range(0, repeat):
            result += decomp

          marker_size = 3 + len(str(number)) + len(str(repeat))

          cursor += number + marker_size

        else:
          result += char
          cursor += 1

      total += len(result)

      if expected:
        assert len(result) == expected[line_index]

      print total

if __name__ == "__main__":
  expected = None
  if "test" in sys.argv[1]:
    expected = [6, 7, 9, 11, 6, 18]
    #expected = [9, 20, 241920, 445]

  main(sys.argv[1], expected)