# from distutils.core import setup
# import py2exe
#
# setup(console=['hello.py'])
import logging

myloger = logging.getLogger("ysl")
myloger.setLevel(logging.INFO)

if __name__ == '__main__':
    myloger.info("123")