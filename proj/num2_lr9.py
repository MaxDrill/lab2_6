#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    d = {5: 'five', 8: 'eight', 10: 'ten'}
    swapped = {value: keys for keys, value in d.items()}
    print(d)
    print(swapped)