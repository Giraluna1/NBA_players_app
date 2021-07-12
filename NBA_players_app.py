#!/usr/bin/python3
""" This is the main file that take endpoint from nba players web
    and  print a list of all pairs of players whose height in inches
    adds up to the integer input to the application. If no matches are found,
    the application will print "No matches found"
"""

import json
from typing import List
import requests
import sys
from os import getenv

if __name__ == "__main__":


    def search_pair(list_players, low, high, diference_h):
        """ implement the binary search algorithm
            complexity O(log n)
        """

        mid = (high + low) // 2
        h_in = int(list_players[mid]['h_in'])

        if low <= high:

            # If diference_h is present at the middle itself
            if h_in == diference_h:
                return mid

            # If diference_h is smaller than mid, then it can only
            # be present in left sub list
            elif h_in > diference_h:
                high = mid - 1

                return search_pair(list_players, low, high, diference_h)
            # Else means diference_h is can only be presente in right sub list
            else:
                low = mid + 1
                return search_pair(list_players, low, high, diference_h)
        # Element is not present in the list_playersay
        else:
            return -1


    def show_players_sumheigh_is_input(input_number):

        if getenv('NBA_ENV') == 'test':
            with open('filestorage.json', 'r') as filestorage:
                data = json.load(filestorage)

        else:
            r = requests.get('http://mach-eight.uc.r.appspot.com/')

            # Obtein the data set
            data = r.json()
        list_players = data.get('values')

        # sort list with key 'h_in'
        list_players.sort(key=lambda player: player['h_in'])
        possible_combinations = []

        # search the pair
        for player_info in list_players:
            first_name = player_info.get('first_name')
            last_name = player_info.get('last_name')
            full_name_1 = first_name + " " + last_name
            first_h = player_info['h_in']
            diference_h = input_number - int(first_h)
            pair = search_pair(list_players, 0, len(list_players) - 1, diference_h)
            if pair is -1:
                pass
            else:
                first_name_2 = list_players[pair].get('first_name')
                last_name_2 = list_players[pair].get('last_name')
                full_name_2 = first_name_2 + " " + last_name_2
                # if is the same player not include
                if full_name_1 == full_name_2:
                    continue
                # Sort the pairs in alphabet
                if first_name < first_name_2:
                    peers = "-{}    {}".format(full_name_1, full_name_2)
                else:
                    peers = "-{}    {}".format(full_name_2, full_name_1)

                # if the combination is in the possible combinations not include
                if peers in possible_combinations:
                    continue
                else:
                    possible_combinations.append(peers)

        try:
            possible_combinations[0]
            print(*possible_combinations, sep = "\n")
        except:
            print('No matches found')

    show_players_sumheigh_is_input(int(sys.argv[1]))
