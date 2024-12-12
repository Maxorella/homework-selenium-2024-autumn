import time

import pytest
from dotenv import load_dotenv


from hw.code.base_case import BaseCase

load_dotenv()


@pytest.mark.usefixtures()
class TestAudience(BaseCase):

    def test_open(self, main_page):
        print("here1")
        time.sleep(1) # TODO убрать
        print("here2")
