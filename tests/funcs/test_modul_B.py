from base import BaseClass

class B(BaseClass):
    def __init__(self):
        BaseClass.__init__(self)

    def test_b_1(self, driver_in):
        driver = driver_in + " + B"
        s = "test modul B, test_b_1 " + driver
        self.log.info("test_b_1 done")
        return s, driver

    def test_b_2(self):
        s = "test modul B, test_b_2"
        print s
        return s
