import types
from pprint import pprint


def flat_generator(list_of_lists):
    main_cursor = 0
    while main_cursor < len(list_of_lists):
        nested_cursor = 0
        while nested_cursor < len(list_of_lists[main_cursor]):
            yield list_of_lists[main_cursor][nested_cursor]
            nested_cursor += 1
        main_cursor += 1


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    for element in flat_generator(list_of_lists_1):
        pprint(element)


if __name__ == '__main__':
    test_2()

