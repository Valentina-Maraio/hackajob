class Solution:

	def run(self, N, M):

		result = []

		for i in range(N, M + 1):
			if i % 3 == 0 and i % 5 == 0:
				result.append("FizzBuzz")
			elif i % 3 == 0:
				result.append("Fizz")
			elif i % 5 == 0:
				result.append("Buzz")
			else:
				result.append(str(i))

		sequence = ",".join(result)
		return sequence