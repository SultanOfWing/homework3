# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

from typing import List


def multi_sum_np(n: int):
    input_list = []
    max_length = 0
    for i in range(n):
        inp = input().split(" ")
        input_list.append(inp)
        if max_length < len(inp):
            max_length = len(inp)

    for i in range(n):
        delta = max_length - len(input_list[i])
        if delta > 0:
            # todo should work, but it don't
            # np.pad(input_list[i], (0, 1))
            for j in range(delta):
                input_list[i].append("0")

    output_list = []
    np_array = np.array(input_list)

    for j in np.rot90(np_array):
        output_list.insert(0, np.sum(np.array(j).astype(np.int64)))

    print(output_list)


def generate_matrix(n: int):
    matrix = np.zeros((n, n))
    np.fill_diagonal(matrix, 1)
    print(matrix)


def transpose_matrix(n: int, m: int):
    matrix = np.round(np.random.rand(n, m) * 10)
    print(matrix)
    print(np.transpose(matrix))


def word_counter(input_list: List[str], word: str):
    counter = dict()
    for word in input_list:
        if word in counter:
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1

    print(counter[word])


# multi_sum_np(2)
# generate_matrix(4)
# transpose_matrix(2, 3)
# word_counter(["chibick", "lol", "kek", "lol"], "lol")

def unique_numbers(input_list: List[int]):
    print(set(input_list))


def fill_set_and_check_if_exists():
    numbers = set()
    while True:
        prev_size = len(numbers)
        numbers.add(input())
        current_size = len(numbers)
        if prev_size == current_size:
            print("Already exists")
        else:
            print("Successfully added")


def emails_manager():
    emails = set()
    while True:
        inp = input().split("::")
        if len(inp) != 2:
            print("Invalid command")

        if inp[0] == "add":
            email = inp[1]
            if email.find("@") >= 0 and email.find(".") >= 0:
                emails.add(email)
                print("Successfully added")
            else:
                print("Invalid format")
        elif inp[0] == "contains":
            print(inp[1] in emails)
        elif inp[0] == "delete":
            email = inp[1]
            if email in emails:
                emails.remove(email)
                print("Successfully deleted")
            else:
                print("This email do not exists")


# unique_numbers([4, 5, 6, 7, 4, 5, 9, 7, 5, 1, 2, 3])
# fill_set_and_check_if_exists()
# emails_manager()

def phonebook_manager():
    phonebook = dict()
    while True:
        inp = input().split(" ")
        if len(inp) == 3:
            if inp[0] == "insert":
                try:
                    int(inp[2])
                    print("Phone successfully added")
                except:
                    print("Phone must be number")
                    continue
                phonebook[inp[1]] = inp[2]
            else:
                print("Unknown command")
        elif len(inp) == 2:
            name = inp[1]
            if name in phonebook:
                if inp[0] == "get":
                    print(phonebook[inp[1]])
                if inp[0] == "delete":
                    del phonebook[name]
                    print("Phone successfully deleted")
            else:
                print("Not found")


phonebook_manager()
