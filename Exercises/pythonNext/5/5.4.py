def check_id_valid(id_number):
    list_id_number = [int(x) for x in str(id_number)]  # convert id_number to list of integers
    iter_list_id_number = iter(range(1, len(list_id_number)))  # need to decrease 1, starting from 0

    for i in iter_list_id_number:
        next(iter_list_id_number)  # skip even numbers
        multiple = int(list_id_number[i]) * 2
        list_id_number[i] = multiple

        if int(multiple) > 9:
            sum_of_digits = multiple % 10 + multiple // 10 % 10  # or use: (sum(divmod(multiple, 10)))
            list_id_number[i] = int(sum_of_digits)

    return sum(list_id_number) % 10 == 0


# print(check_id_valid(123456782))
# print(check_id_valid(123456780))

# list((str(id_number))) give strings
# "".join(list_id_number)

class IDIterator:
    def __init__(self, id):
        self._id = int(id)

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            self._id += 1

            if self._id == 999999999:
                raise StopIteration

            if check_id_valid(self._id):
                return self._id


def id_generator(id_number):
    id_number = int(id_number)
    while True:
        id_number += 1
        if check_id_valid(str(id_number)):
            yield id_number


def main():
    user_id_input = input("Enter id: ")
    gen_or_it_input = input("Generator or Iterator? (gen/it)? ")

    if gen_or_it_input == "gen":
        generator_next_id = id_generator(user_id_input)
        for id in range(10):
            print(next(generator_next_id))
    elif gen_or_it_input == "it":
        iter_id = iter(IDIterator(user_id_input))
        for id in range(10):
            print(next(iter_id))
    else:
        print("No gen or it")


main()
