set_a_string = ['0.866', '-0.166i', '0.333j', '0.333k']
#set_b_string = ['2', '3i', '0', '0']
#set_a_string = [['0.8662', '0.166i3i', '0.333j0', '0.333k0'], ['0.166i2', '0.8663i', '0.333j0', '-0.333k0'], ['0.8660', '-0.166i0', '0.333j2', '0.333k3i'], ['0.8660', '0.166i0', '-0.333j3i', '0.333k2']]
set_b_string = ['0.866', '-0.166i', '-0.333j', '-0.333k']
#set_a_string = [[0.866, '~'], [-0.166, 'ib'], [0.333, 'jc'], [0.333, 'kd']]
#set_b_string = [[0.866, '~'], [-0.166, 'if'], [0.333, 'jg'], [0.333, 'kh']]
def seperate_string(string_val):
	lookup = ['i', 'j', 'k']
	for index, bit in enumerate(string_val):
		if bit in lookup:
			str_index = index
		else:
			str_index = '~'

	if str_index is '~':

			variable = [float(string_val), str_index]
			return variable
	else:
		try:
			variable = [float(string_val[:str_index]), string_val[str_index]]
			return variable

		except:
			variable = 'Something in the string cannot be turned into numbers'
			return variable
	


def add_quaternions(set_a_string, set_b_string):
	fix_set_a = []

	fix_set_b = []

	solution = []
	for sets in set_a_string:
		fix_set_a.append(seperate_string(sets))

	for sets in set_b_string:
		fix_set_b.append(seperate_string(sets))

	for index, set_a_value in enumerate(fix_set_a):
		solution_set = [set_a_value[0] + fix_set_b[index][0], set_a_value[1]]
		solution.append(solution_set)
	
	for sets in solution:
		for sub_set in sets:
			if sub_set == '~':
				sets.remove(sub_set)

	return solution	

def multiply_single_quaternion(set_a_string, set_b_string):
	# first set is multiplied by scalar, second set by i, third by j, fourth by k. Do the neccesary conversion
	identity_table = {'ij':'k', 'jk':'i', 'ki':'j', 'ji':'-k', 'kj':'-i', 'ik':'-j', 'ii': -1, 'jj': -1, 'kk': -1}
	fix_set_a = []

	fix_set_b = []

	solution_set = []

	complex_set = []

	return_quaternion = []

	for sets in set_a_string:
		fix_set_a.append(seperate_string(sets))

	for sets in set_b_string:
		fix_set_b.append(seperate_string(sets))
	
	
	for set_b_value in fix_set_b:
		for set_a_value in fix_set_a:
			val_a = set_a_value[0] * set_b_value[0]
			val_b = set_a_value[1] + set_b_value[1]
			solution_set.append([val_a, val_b])

	for sets in solution_set:
		for sub_set in sets:
			if sub_set == '~~':
				sets.remove(sub_set)

	for sets in solution_set:
		if len(sets) > 1:
			if '~' in sets[1]:
				new_string = sets[1].replace('~', '')
				sets[1] = new_string

	for sets in solution_set:
		if len(sets)>1:
			for key, val in identity_table.iteritems():
				if sets[1] == key:
					sets[1] = val

			
	for sets in solution_set:
		if len(sets)>1:
			if isinstance(sets[1], int):
				sets = [sets[0] * sets[1], sets[1]]
			else:
				if '-' in sets[1]:
					sets = [sets[0]*-1, sets[1][-1]]
				else:
					sets = [sets[0], sets[1]]
			complex_set.append(sets)
		else:
			sets = [sets[0]]
			complex_set.append(sets)
	'''
	bugfix sequence
	for index, item in enumerate(complex_set):
		if len(item)>1:
			if item[1] == 'k':
				print index
	'''
	return_set_real = [complex_set[0][0] + complex_set[5][0] + complex_set[10][0] + complex_set[15][0]]
	return_set_i = [complex_set[1][0] + complex_set[4][0] + complex_set[11][0] + complex_set[14][0], 'i']
	return_set_j = [complex_set[2][0] + complex_set[7][0] + complex_set[8][0] + complex_set[13][0], 'j']
	return_set_k = [complex_set[3][0] + complex_set[6][0] + complex_set[9][0] + complex_set[12][0], 'k']
	
	return_quaternion = [return_set_real, return_set_i, return_set_j, return_set_k]
	
	return return_quaternion


print multiply_single_quaternion(set_a_string, set_b_string)