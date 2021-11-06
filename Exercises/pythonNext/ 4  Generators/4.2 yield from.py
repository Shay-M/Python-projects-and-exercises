def city_generator():
    print("Starting")
    yield "London"
    yield "Berlin"
    yield "Amsterdam"


city = city_generator()
print(city)  # <generator object city_generator at 0x000001FCEB486F90>

print(next(city))


# Starting
# London
# Berlin
# Amsterdam


def add_jerusalem_generator():
    yield from city_generator()
    yield "Jerusalem"


patriot = add_jerusalem_generator()
print(next(patriot))
print(next(patriot))
print(next(patriot))
print(next(patriot))


# https://courses.campus.gov.il/courses/course-v1:CS+GOV_CS_nextpy102+2_2020/courseware/727f560c14e24ea5bfd4183fe380afb0/773319cf7277413a98ae483f720bfae2/?child=first


def gen4():
    x = 0
    while x < 3:
        yield x
        x += 1


s = gen4()
print(next(s))  # 0
print(next(s))  # 1
print(next(s))  # 2
