from pprint import pprint


class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        print('Enter the loop...')
        self.nested_list_cursor = -1
        self.main_list_cursor = 0
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if self.nested_list_cursor == len(self.main_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.nested_list_cursor = 0
        if self.main_list_cursor == len(self.main_list):
            raise StopIteration

        return self.main_list[self.main_list_cursor][self.nested_list_cursor]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    for element in FlatIterator(list_of_lists_1):
        pprint(element)
    

if __name__ == '__main__':
    test_1()
