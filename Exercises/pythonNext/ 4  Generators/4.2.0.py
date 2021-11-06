with open("capitals.txt") as file:
    single_line_gen = (line for line in file)
    # France, Paris
    capitals_and_cities = (l.replace("\n", "").split(",") for l in single_line_gen)
    # ['France', 'Paris']
    capitals_dict = dict(capitals_and_cities)

print(capitals_dict["israel"])
