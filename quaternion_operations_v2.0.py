import math

quaternion_a = [0.866, -0.166, 0.333, 0.333]
quaternion_b = [0.866, -0.166, -0.333, -0.333]

def multiply_quaternion(quaternion_a, quaternion_b):

	identity_table = {'ij':'k', 'jk':'i', 'ki':'j', 'ji':'-k', 'kj':'-i', 'ik':'-j', 'ii': -1, 'jj': -1, 'kk': -1}
	
	product = []

	for q_b_num in quaternion_b:
		for q_a_num in quaternion_a:
			value = q_a_num * q_b_num
			product.append(value)

	real_num = [product[0] + (-product[5]) + (-product[10]) + (-product[15])]
	i_num = [product[1] + product[4] + product[11] + (-product[14])]
	j_num = [product[2] + (-product[7]) + product[8] + product[13]]
	k_num = [product[3] + product[6] + (-product[9]) + product[12]]
	
	return [real_num[0], i_num[0], j_num[0], k_num[0]]


def add_quaternions(quaternion_a, quaternion_b):

	answer = []

	for index, q_a_values in enumerate(quaternion_a):
		q_sum = q_a_values + quaternion_b[index]
		answer.append(q_sum)

	return answer


def normalize_vector(vector):

	squares = []

	for numbers in vector:
		new_num = numbers**2
		squares.append(new_num)

	denominator = math.sqrt(sum(squares))

	return [j/denominator for j in vector] 


def dir_to_quat(vector, angle):

	norm_vector = normalize_vector(vector)

	complex_number = [i*math.sin(math.radians(angle/2)) for i in norm_vector]

	scalar = math.cos(math.radians(angle/2))

	return [scalar] + complex_number

def conjugate(quaternion):

	conjugated = [quaternion[0], -quaternion[1], -quaternion[2], -quaternion[3]]

	return conjugated

def rotate(axis_of_rotation, angle, vector_to_rotate):

	q = dir_to_quat(axis_of_rotation, angle)

	p = [0] + vector_to_rotate

	q_conjugate = conjugate(q)

	# q * p * q(conjugate)

	q_b = multiply_quaternion(q, p)

	solution = multiply_quaternion(q_b, q_conjugate)
	
	return solution[1:]
	

#print normalize_vector([1, 2, 2])

#print multiply_quaternion(quaternion_a, quaternion_b)

print rotate([1,2,2], 60, [2, 3, 0])
