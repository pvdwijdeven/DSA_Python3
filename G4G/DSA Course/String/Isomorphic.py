def are_isomorphic(str1,str2):
	mp1 = {}
	mp2 = {}
	s = len(str1)
	if s != len(str2):
		return False
	for i in range(s):
		if str1[i] in mp1:
			if mp1[str1[i]] != str2[i]:
				return False
		else:
			mp1[str1[i]] = str2[i]
		if str2[i] in mp2:
			if mp2[str2[i]] != str1[i]:
				return False
		else:
			mp2[str2[i]] = str1[i]
	return True
