#! /home/dunyu/anaconda3/envs/testenv/bin/python

def talk():
    print("package is working")

class test_class():
    def __init__(self, data:int = 0):
        self.data = data
        pass

    def talk(self):
        print("class is working")

    def print_data(self):
        print("data is",self.data)