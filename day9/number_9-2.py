import sys

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def handle_marker(cursor, line):
  initial_cursor = cursor

  total_length = 0

  x_pos = line[cursor:].find('x') + cursor
  number = int(line[cursor + 1 : x_pos])
  #print "number"
  #print number
  end_par_pos = line[x_pos:].find(')') + x_pos
  repeat = int(line[x_pos + 1 : end_par_pos])

  #print "begin marker"
  #print "(%sx%s)" % (number, repeat)

  cursor = end_par_pos + 1

  end_of_treatment = end_par_pos + number + 1

  recur = 0

  #print "current_cursor"
  #print cursor

  #print "end_of_treatment"
  #print end_of_treatment

  while cursor < end_of_treatment and recur < 5:
    #print "current_cursor"
    #print cursor
    #print line[cursor]
    if cursor < end_of_treatment and len(line) > cursor and line[cursor] == '(':
      #print "handle_marker in while"
      (length, cursor) = handle_marker(cursor, line)
      total_length += length

    is_alpha = True
    x = 1
    while is_alpha:
      pos = end_par_pos + x
      if len(line) > pos and pos < end_of_treatment and line[pos] in alpha:
        x +=1
      else:
        is_alpha = False
    nb_chars_before_new_marker = x -1

    recur+=1

    cursor += nb_chars_before_new_marker

  return repeat * (nb_chars_before_new_marker + total_length), cursor

def main(arg, expected=None):
  total = 0

  with open(arg) as f:
    for line_index, line in enumerate(f):
      print line

      line = line.replace("\n", "")

      cursor = 0
      tot_length = 0

      for i, char in enumerate(line):
        if i < cursor:
          continue

        if char == '(':
          length, cursor = handle_marker(cursor, line)
          tot_length += length

          #print "tot_length after markers"
          #print tot_length

        else:
          tot_length += 1
          cursor += 1

        #print "tot_length after letter"
        #print tot_length

      total += tot_length

      if expected:
        print tot_length
        assert tot_length == expected[line_index]
        print "GOOD"

      print total

if __name__ == "__main__":
  expected = None
  if "test" in sys.argv[1]:
    expected = [9, 20, 241920, 445]

  main(sys.argv[1], expected)