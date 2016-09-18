import StatMaker
from sys import argv
import numpy as np
from sknn.mlp import Regressor, Layer
import itertools

COLUMNS = ["Sinker", "Split", "Curve", "Change", "Slider", "Cutter",
           "Fourseam"]


def main():
    stats = StatMaker.StatMaker()
    stats.parse(argv[1], argv[2])
    player = stats.players["Edwin Encarnacion"]

    x = []
    y = []
    x_ = []

    for p in COLUMNS:
        x += [player.pitch_freq[p]]
        y += [player.tb_aves[p]]
        x_ += [stats.opp_pitch[p]]

    x_ = list(itertools.chain(*x_))

    x_ = np.array([x_])
    x = np.array([x])
    y = np.array([y])
    nn = Regressor(
        layers=[
            Layer("Rectifier", units=100),
            Layer("Softmax")],
        learning_rate=0.01,
        n_iter=100)
    nn.fit(x, y)

    y_example = nn.predict(x_)

    i = 0
    for each in y_example:
        print(COLUMNS[i] + " is:"+ str(each))
        i += 1
if __name__ == '__main__':
    main()
