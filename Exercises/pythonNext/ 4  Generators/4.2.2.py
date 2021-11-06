def parse_ranges(ranges_string):  # "1-2,4-4,8-10"
    ranges = (range.split("-") for range in ranges_string.split(","))
    # print(next(ranges))  # ['1', '2']
    generator_of_range = (num for first, second in ranges for num in range(int(first), int(second) + 1))

    return list(generator_of_range)


print(parse_ranges("1-2,4-4,8-10"))
print(parse_ranges("0-0,4-8,20-21,43-45"))

##################################################################

ranges = (range.split("-") for range in "1-2,4-4,8-10".split(","))
# print(next(ranges))  # ['1', '2']
for star, stop in ranges:
    print(star)
    # 1
    # 4
    # 8
