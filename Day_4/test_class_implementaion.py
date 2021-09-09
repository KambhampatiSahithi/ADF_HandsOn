import pytest
import class_implementaion as test_code



test_list = ["this", "sample", "to", "file", "madam", "ADF", "dancing", "jumping", "to"]
uniq_list = ["l", "hh", "rhf", "DT", "s", "k2", "ADFS"]


def test_prefix1():
    result = test_code.FileOperations.prefix_to(test_list)
    assert result == 2


def test_post2():
    result = test_code.FileOperations.postfix_ing(test_list)
    assert result == 2


def test_repeated():
    result = test_code.FileOperations.most_repeated(test_list)
    assert result == "to"


def test_palindrome():
    result = test_code.FileOperations.find_palindrome(test_list)
    result = "".join(result)
    assert result == "madam"


def test_unique():
    result = test_code.FileOperations.uniqfileoper(test_list)
    assert result == "th-s-s-mpl-t-f-l-m-d-m-DF-d-nc-ng-j-mp-ng-t"


''' Failed cases for methods examples'''


def test_palindrome_failed():
    result = test_code.FileOperations.find_palindrome(test_list)
    result = "".join(result)
    assert result != "mada"
