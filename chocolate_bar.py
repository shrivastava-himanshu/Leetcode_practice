def make_chocolate(small, big, goal):
  big_bar = 0
  for big_bar in range(big):

    if goal >= 5:
      goal =goal - 5

    else:
      break
  small_bar = goal
  return small_bar


if __name__ == '__main__':
    s = 4
    b = 1
    g = 9
    print(make_chocolate(s,b,g))
