from collections import defaultdict
import json


class StatMaker():
    class Player():
        def __init__(self, pitch_rate, pitch_freq):
            self.tb_aves = pitch_rate
            self.pitch_freq = pitch_freq

    def __init__(self):
        self.players = defaultdict(StatMaker.Player)
        self.opp_pitch = defaultdict(list)

    def parse(self, train_name, test_name):
        with open(train_name) as data:
            j = json.load(data)
            for player in j:
                new_player = StatMaker.Player(
                    self.create_y_train(player["pitches"]),
                    self.create_x_train(player["pitches"]))

                self.players[player['name']] = new_player
        with open(test_name) as data:
            j = json.load(data)
            self.create_x_test(j)

    def create_y_train(self, json_pitches):
        pitches = defaultdict(float)
        for p in json_pitches:
            name = p[0]
            p = [float(x) for x in p[1:]]

            if p[0]:
                tb_ave = (p[3]+p[5]+2.0*p[6]+3.0*p[7]+4.0*p[9])/p[0]
            pitches[name] = tb_ave
        return pitches

    def create_x_train(self, json_pitches):
        pitches = defaultdict(float)
        for p in json_pitches:
            name = p[0]
            p = [float(x) for x in p[1:]]
            if p[1]:
                pitch_freq = p[0] / p[1]
            pitches[name] = pitch_freq
        return pitches

    def create_x_test(self, json_opp_pitch):
        for each in json_opp_pitch:
            for p in each["pitches"]:
                self.opp_pitch[p[0]] += [float(p[1])]

        for key, value in self.opp_pitch.items():
            self.opp_pitch[key] = [sum(value) / float(len(value)) / 20.0]

if __name__ == '__main__':
    from sys import argv
    tmp = StatMaker()
    tmp.parse(argv[1])

    for name, pitches in tmp.players.items():
        print(name)
        for key, value in pitches.tb_aves.items():
            print(key + " tb_ave is:" + str(value))
        for key, value in pitches.pitch_freq.items():
            print(key + " pitch_freqx is:" + str(value))

