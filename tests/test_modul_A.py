import funcs.test_modul_B as test_modul_B
from funcs.base import BaseClass

class A(BaseClass):
    def __init__(self):
        BaseClass.__init__(self)
        self.driver_var = "Firefox A"


    def test_a_1(self):
        b = test_modul_B.B()
        a, self.driver_var = b.test_b_1(self.driver_var)
        print "result str :", a
        print "result driver_var :", self.driver_var
        self.log.info("test_a_1 success!")


    def test_a_2(self):
        print "test modul A, test_a_2"