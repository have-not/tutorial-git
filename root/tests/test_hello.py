import unittest as UT
import hello    as H

class TestForHello(UT.TestCase):
    def test_hello_01(self):
        self.assertEqual( H.getGreetMsg()
                        , "hello!"
                        )

    def test_hello_02(self):
        self.assertEqual( H.getGreetMsg(12)
                        , "hello!"
                        )

    def test_hello_03(self):
        self.assertEqual( H.getGreetMsg(8)
                        , "good morning!"
                        )



if (__name__ == "__main__"):
    UT.main()

