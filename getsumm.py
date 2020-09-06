def get_summ(one, two, delimiter='&'):
	one=str.upper(one)
	two=str.upper(two)
	summ=one+delimiter+two
	print(summ)

get_summ('Learn', 'python')