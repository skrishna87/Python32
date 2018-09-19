import unittest
import test
class testcap(unittest.testcase):

	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multi_words(self):
		text = 'monty python'
		result = 'monty python'
		self.assertEqual(result, 'Monty Python')

if __name__ == __main__:
	unittest.main()ClassName(object):
		"""docstring for ClassName"""
		def __init__(self, arg):
			super(ClassName, self).__init__()
			self.arg = arg
			