import nose

# nosetests test.module
# nosetests another.test:TestCase.test_method
# nosetests a.test:TestCase
# nosetests /path/to/test/file.py:test_function

if __name__== '__main__':
    #nose.main(argv=['','-v'])
    #nose.main(argv=['', 'tests/tests/test_modul_B.py','-v'])
    #nose.main(argv=['', 'tests/tests/test_modul_B.py:test_b_2','-v'])
    nose.main(argv=['', 'tests/tests/test_modul_B.py:test_b_2','-v', '-s'])
