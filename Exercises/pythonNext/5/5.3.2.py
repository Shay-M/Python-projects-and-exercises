freqs = {"la": 55,
         "si": 61.74,
         "do": 65.41,
         "re": 73.42,
         "mi": 82.41,
         "fa": 87.31,
         "sol": 98,
         }


class MusicNotes:
    def __init__(self):
        self.freqs_index = -1
        self._list_of_freqs = [(freq * (i ** 2)) for freq in freqs.values() for i in range(1, 5)]
        self._list_of_freqs.sort()

    def __iter__(self):
        return self

    def __next__(self):
        if self.freqs_index >= len(self._list_of_freqs) - 1:
            raise StopIteration()
        self.freqs_index += 1
        return self._list_of_freqs[self.freqs_index]


############################################# יוצא כפול
freqs = [55, 61.74, 65.41, 65.41, 73.42, 82.41, 87.31, 98]


class MusicNotes:
    def __iter__(self):
        self.__octave = 0
        self.__note = -1
        return self

    def __next__(self):

        self.__note += 1
        if self.__note == len(freqs):
            self.__note = 0
            self.__octave += 1

        if self.__octave == 5:
            raise StopIteration

        return freqs[self.__note] * 2 ** self.__octave


########
notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)
