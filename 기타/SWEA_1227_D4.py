for test_case in range(1, 11):
	maze = []
	pos = (0, 0)
	goal =(0, 0)
	last_pos =[]
	ans = 0

	num = input()

	for i in range(0, 100, 1):
		a = list(map(int, list(input())))
		if 3 in a:
			goal = (i, a.index(3))
		if 2 in a:
			pos = (i, a.index(2))
		maze.append(a)

	last_pos.append(pos)
	while True:
		if pos == goal:
			ans = 1
			break
		else:
			if pos[0] + 1 < 100 and not (pos[0] + 1, pos[1]) in last_pos and not maze[pos[0] + 1][pos[1]] in [1, 4]:
				last_pos.append(pos)
				pos = (pos[0] + 1, pos[1])
			elif pos[1] + 1 < 100 and not (pos[0], pos[1] + 1) in last_pos and not maze[pos[0]][pos[1] + 1] in [1, 4]:
				last_pos.append(pos)
				pos = (pos[0], pos[1] + 1)
			elif pos[0] - 1 >= 0 and not (pos[0] - 1, pos[1]) in last_pos and not maze[pos[0] - 1][pos[1]] in [1, 4]:
				last_pos.append(pos)
				pos = (pos[0] - 1, pos[1])
			elif pos[1] - 1 >= 0 and not (pos[0], pos[1] - 1) in last_pos and not maze[pos[0]][pos[1] - 1] in [1, 4]:
				last_pos.append(pos)
				pos = (pos[0], pos[1] - 1)
			else:
				maze[pos[0]][pos[1]] = 4
				pos = last_pos[-1]
				del last_pos[-1]
				if len(last_pos) == 0:
					break

	del maze[:]
	print('#' + str(test_case) + ' ' + str(ans))