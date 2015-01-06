-------------------------------------------
'''
>>> 1 == 1
False
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()

-------------------------------------------

import unittest

class BasicsTestCase(unittest.TestCase):

    def test_find_name(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 2)

if __name__ == '__main__':
    unittest.main()

-------------------------------------------

# content of test_example.py, run with $ py.test

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

-------------------------------------------

# run tests over the directory
$ nosetest

---------------------------------------------

filename = raw_input('Enter a file name: ')
try:
    f = open(filename, "r")
except:
    print 'There is no file named', filename

raise Exception('Invalid config file: expecting keys "aws_access_key", "aws_secret_key", "bucket"')
g = lambda x: x ** 2

try:
    operation, filename = sys.argv[1:]
except ValueError:
    print __doc__
    sys.exit(2)

subprocess.call()
try:
    response = urllib2.urlopen()

-----------------------------------------------

import subprocess,os

os.system('ls')
subprocess.call(['ls', '-1'], shell=True)
