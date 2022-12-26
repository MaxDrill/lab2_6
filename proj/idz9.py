#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    train = []
    while True:
        info = input(">>> ").lower()
        if info == 'exit':
            break

        elif info == 'add':
            dest = input("What destination do you need? ")
            numb = int(input("What number of the train? "))
            date = float(input("What time do you need? "))
            trainDct = {
                'destination': dest,
                'number_train': numb,
                'flight_date': date,
            }
            train.append(trainDct)
            if len(train) > 1:
                train.sort(key=lambda item: item.get('flight_date', ''))

        elif info == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 18
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^18} |'.format(
                    "№",
                    "Destination",
                    "Number of the train",
                    "Flight Date"
                )
            )
            print(line)

            for i, item in enumerate(train, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>18} |'.format(
                        i,
                        item.get('destination', ''),
                        item.get('number_train', ''),
                        item.get('flight_date', 0)
                    )
                )
            print(line)

        elif info.startswith('select'):
            t = input("enter your destination: ")
            count = 0
            for i in train:
                if i.get('destination') == t:
                    count += 1
                    print(
                        '{:>4}: {} {} {}'.format(
                            count,
                            i.get('destination', ''),
                            i.get('flight_date'),
                            i.get("number_train")
                        )
                    )
            if count == 0:
                print("We couldn't find this type of plane")

        elif info == 'help':
            print("command list:\n")
            print("add - add information about a flight;")
            print("list - display the flight schedule;")
            print("select <type> - select destination;")
            print("help - show reference;")
            print("exit - leave a program.")
        else:
            print(f"unknown command {info}", file=sys.stderr)