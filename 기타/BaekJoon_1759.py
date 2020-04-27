L, C = list(map(int, input().split()))

alphabet = list(input().split())
alphabet.sort()

def lexicographical_order(idx, alphabet_list, combis):
	for i in range(idx, len(alphabet_list)):
		if len(combis) != L - 1:
			lexicographical_order(i+1, alphabet_list, combis + [alphabet_list[i]])
		else:
			condition = len(set(combis+[alphabet_list[i]]) - {'a','i','u','e','o'})
			if not condition in [0, 1, len(set(combis+[alphabet_list[i]]))]:
				print(''.join(combis+[alphabet_list[i]]))

lexicographical_order(0, alphabet, [])