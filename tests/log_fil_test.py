import logging
from funcs.base import BaseClass


class A(BaseClass):
    def __init__(self):
    #@classmethod
    #def setupClass(self):
        BaseClass.__init__(self)
        #self.log = logging.getLogger("app")
        self.log.info("Setup Class finished success")
        print "Setup Class finished success"


    def test_one(self):
        self.log.critical("message")
        print "test_one finished success"

#if __name__== '__main__':
    #nose.main(argv=['', '-v'])
    #nose.main(argv=['', 'log_fil_test.py', '-v','-s'])
    #nose.main(argv=['', 'tests/test_modul_A.py','-v', '-s'])