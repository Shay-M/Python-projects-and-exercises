import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
yonatan_hakatan_notes = []
for note in notes.split("-"):
    # yonatan_hakatan_notes.extend(note.split(","))
    yonatan_hakatan_notes.append(note.split(","))

for note in yonatan_hakatan_notes:
    winsound.Beep(freqs[note[0]], int(note[1]))

# player = iter (yonatan_hakatan_notes)
# print(next(player))

##################################################
numbers = iter(list(range(1, 101)))
for i in numbers:
    next(numbers)
    print(i)
