import pytest
from main import merge_sort_count,Participant,find_participant_with_least_inversions,create_order


def test_zero_inv():
    order = {1:0, 2:1, 3:2}
    skills = [1,2,3]
    assert merge_sort_count(skills, order) == ([1,2,3], 0), "Should be 0 inversions"

def test_one_inv():
    order = {1:0, 2:1, 3:2}
    skills = [2,1,3]
    assert merge_sort_count(skills, order) == ([1,2,3], 1), "Should be 1 inversion"

def test_two_inv():
    order = {1:0, 2:1, 3:2}
    skills = [2,3,1]
    assert merge_sort_count(skills, order) == ([1,2,3], 2), "Should be 2 inversions"

def test_three_inv():
    order = {1:0, 2:1, 3:2}
    skills = [3,2,1]
    assert merge_sort_count(skills, order) == ([1,2,3], 3), "Should be 3 inversions"

def test_with_lists_of_8_elements():
    order = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7}
    skills = [8,7,6,5,4,3,2,1]
    assert merge_sort_count(skills, order) == ([1,2,3,4,5,6,7,8], 28), "Should be 28 inversions"

def test_with_special_order():
    order = {8:0, 7:1, 6:2, 5:3, 4:4, 3:5, 2:6, 1:7}
    skills = [8,7,6,5,4,3,2,1]
    assert merge_sort_count(skills, order) == ([8,7,6,5,4,3,2,1], 0), "Should be 0 inversions"

def integration_test_with_participants():
    """
    Jorge,2,6,1,4,3,5,7,8
    Diego,1,3,5,4,8,2,6,7
    Daniela,7,8,2,1,4,3,5,6
    Thiago,8,1,5,7,2,6,3,4
    Marcela,8,1,7,2,5,3,4,6
    """

    participants = [
        Participant("Jorge", [2,6,1,4,3,5,7,8]),
        Participant("Diego", [1,3,5,4,8,2,6,7]),
        Participant("Daniela", [7,8,2,1,4,3,5,6]),
        Participant("Thiago", [8,1,5,7,2,6,3,4]),   
    ]

    captain = Participant("Marcela", [8,1,7,2,5,3,4,6])

    assert find_participant_with_least_inversions(participants, captain) == participants[0], "Should be Jorge"

def test_create_order_gives_a_dict_with_index_in_revers_order_than_participant():
    participant = Participant("Jorge", [2,6,1,4,3,5,7,8])
    assert create_order(participant) == {8:0, 7:1, 5:2, 3:3, 4:4, 1:5, 6:6, 2:7}, "Should be a dict with index in revers order than participant skills"