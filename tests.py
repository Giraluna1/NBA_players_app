#!/usr/bin/python3
""" This module is for test enviroment """

import unittest
from NBA_players_app import show_players_sumheigh_is_input

import os

peers = show_players_sumheigh_is_input(139)
class test_show__players_sumheigh_is_input(unittest.TestCase):
    """ Test for the core download_players.py """

    def test_find_pair(self):

        self.assertIn(show_players_sumheigh_is_input(139), "-Mike Wilks    Nate Robinson")
