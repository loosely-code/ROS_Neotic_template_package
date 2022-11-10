#! /home/dunyu/anaconda3/envs/testenv/bin/python

import lib_python.test_lib as test_lib

if __name__ == '__main__':
    example = test_lib.test_class(data=10)
    test_lib.talk()
    example.talk()
    example.print_data()


