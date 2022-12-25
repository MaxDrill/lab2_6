#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {
        "1a": 30, "1b": 31, "2a": 29, "2b": 28, "3a": 26, "3b": 16,
        "4a": 18, "4b": 34, "5a": 29, "5b": 30, "6а": 30, "6b": 28,
        "7а": 27, "7b": 26, "8а": 25, "8b": 28, "9а": 29, "9b": 27,
        "10а": 29, "10b": 32, "11а": 25, "11b": 24, "5а": 18, "1c": 13
        }
    school["2a"] = 16
    school["1c"] = 21
    del school["8b"]
    print(f"The total number of students enrolled in school is: {sum(school.values())}")