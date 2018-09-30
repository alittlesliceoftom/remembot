import unittest
from remembot.remembot_classes import *


class TestRemembot(unittest.TestCase):

    def setup(self):

        return

    def test_remember_item(self):
        i = item_to_remember(name="Spotify on engineering", msg="Innovation >> Predictability ",
                             link="https://www.youtube.com/watch?v=R2o-Xm3UVjs")
        u = user(name='Tom')
        u.remember_item(i)
        u.remember_item(i)
        u.remember_item(i)
        print(u.items_to_remember)
        assert len(u.items_to_remember) <2
        return


    # def test_remind_item(self):
    #     u.remind_user(i.name) ##check you get a slack!

if __name__ == '__main__':
    print('starting tests')
    unittest.main()