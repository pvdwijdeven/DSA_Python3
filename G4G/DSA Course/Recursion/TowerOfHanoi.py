def tower_of_Hanoi(N, fromm, to, aux):
	if N == 1:
		print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " +
		      str(to))
		return 1
	res = 0
	res += tower_of_Hanoi(N=N - 1, fromm=fromm, to=aux, aux=to)
	print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " +
	      str(to))
	res += 1
	res += tower_of_Hanoi(N=N - 1, fromm=aux, to=to, aux=fromm)
	return res


if __name__ == "__main__":
	N = 3
	# A, C, B are the name of rods
	print(tower_of_Hanoi(N=N, fromm="A", to="C", aux="B"))
