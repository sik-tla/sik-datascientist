
import pytest

import webscraping.main_web as main_web
from webscraping.main_web import Spider



def test_main():
    """Test main function"""
    # main_web.sik_ulr("https://www.sik.dk/")
    test_class = Spider("https://www.sik.dk/")
    breakpoint()





