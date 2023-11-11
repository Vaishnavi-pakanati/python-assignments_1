_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
_flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
_sharp_set = {'C', 'G', 'D', 'A', 'a', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#'}


class Scale:
    def __init__(self, tonic: str):
        self.tonic = tonic

    def chromatic(self):
        t = self.tonic[0].upper() + ('' if len(self.tonic) == 1 else self.tonic[1])
        res = [t]
        if self.tonic in _sharp_set:
            idx = _sharp.index(t)
            idx = (idx + 1) % 12
            while len(res) < 12:
                res.append(_sharp[idx])
                idx = (idx + 1) % 12
        else:
            idx = _flat.index(t)
            idx = (idx + 1) % 12
            while len(res) < 12:
                res.append(_flat[idx])
                idx = (idx + 1) % 12
        return res

    def interval(self, intervals):
        t = self.tonic[0].upper() + ('' if len(self.tonic) == 1 else self.tonic[1])
        res = [t]
        if self.tonic in _sharp_set:
            idx = _sharp.index(t)
            for step in [1 if c == 'm' else (2 if c == 'M' else 3) for c in intervals]:
                idx = (idx + step) % 12
                res.append(_sharp[idx])
        else:
            idx = _flat.index(t)
            for step in [1 if c == 'm' else (2 if c == 'M' else 3) for c in intervals]:
                idx = (idx + step) % 12
                res.append(_flat[idx])
        return res
