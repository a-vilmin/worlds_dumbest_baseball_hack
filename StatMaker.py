from collections import defaultdict
import json


class StatMaker():
    def __init__(self):
        self.name = ""
        self.pitch_rate = defaultdict(float)
        self.hit_rate = defaultdict(float)

    def parse(self, f_name):
        j = json.loads(f_name)
        print(j['name'])

if __name__ == '__main':
    from sys import argv
    tmp = StatMaker()
    tmp.parse(argv[1])
    
