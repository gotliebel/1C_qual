from difflib import SequenceMatcher


def compare_two_files(file_1, file_2):
    with open(file_1, 'r') as first:
        data_1 = first.read().replace('\n', '')
    with open(file_2, 'r') as second:
        data_2 = second.read().replace('\n', '')

    matcher = SequenceMatcher(None, data_1, data_2)
    return matcher.ratio()
