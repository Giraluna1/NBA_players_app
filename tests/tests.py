#!/usr/bin/python3
""" This module is for test enviroment """

import unittest
from core.NBA_players_app import show_players_sumheigh_is_input

import os

class test_show__players_sumheigh_is_input(unittest.TestCase):
    """ Test for the core download_players.py """

    def test_find_pair(self):
        """ test if the output find the correct peer"""
        self.assertTrue("-Mike Wilks    Nate Robinson\n-Brevin Knight    Nate Robinson", show_players_sumheigh_is_input(139))

    def test_not_found_pair(self):
        """ Test if not found the peer"""
        self.assertTrue("No matches found", show_players_sumheigh_is_input(100))

    def test_not_repeat_combination(self):
        """ Test that single pair combination"""
        self.assertTrue("-Yao Ming      Zydrunas Ilgauskas", show_players_sumheigh_is_input(177))
        self.assertFalse(show_players_sumheigh_is_input(177), "-Zydrunas      Ilgauskas Yao Ming")

    def test_not_is_the_same(self):
        """ Test if not is the same player"""
        self.assertFalse(show_players_sumheigh_is_input(140), "-Mike Wilks    Mike Wilks")
