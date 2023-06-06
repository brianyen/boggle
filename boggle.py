import copy

real_words = []

with open("bogglelist.txt") as f:
  for word in f.readlines():
    real_words.append(word.strip("\n"))

def solve(arr):
  sol = []
  for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
      sol += recurse(arr, i, j, "", [], [])
  return sol

def recurse(arr, row, col, word, answers, checked):
  cell = arr[row][col]
#  print("checked:", checked, "\nword:", word, "\ncell:", cell)
  checked.append([row, col])
  word += cell

  options = []
  for i in range(row - 1, row + 2):
    for j in range(col - 1, col + 2):
      if (i < 0) or (j < 0):
        continue
      try:
        arr[i][j]
      except IndexError:
        continue
      if [i, j] in checked:
        continue
      else:
        options.append([i, j])

  if (len(word) > 2) and (not (word in answers)):# and (word in real_words):
    answers.append(word)
  if len(options) == 0:
    return answers
  else:
    for pos in options:
      current_checked = copy.copy(checked)
      results = recurse(arr, pos[0], pos[1], word, [], current_checked)
      if (type(results) == list) and (len(results) > 0):
        answers += results

  return answers


def construct_board(input_list):
  input_arr = []
  arr_el = []
  for i in range(0, len(input_list)):
    if input_list[i] == "/":
      input_arr.append(arr_el)
      arr_el = []
    else:
      arr_el.append(input_list[i])
  input_arr.append(arr_el)
  return input_arr


print("type in board with \"/\" separating rows, e.g.: abc/def/ghi for a 3x3")

board = input()
solution = solve(arr=construct_board(board))
print("FINAL:", len(solution), solution)