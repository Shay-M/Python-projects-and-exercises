def read_file(file_name):
    print('__CONTENT_START__')
    try:
        file_object = open(file_name, 'r')
    except:
        print('__NO_SUCH_FILE__')
    else:
        print(file_object.read())
        file_object.close()
    finally:
        print('__CONTENT_END__')


def main():
    read_file("one_lined_file.txt")
    read_file("file_does_not_exist.txt")


main()
