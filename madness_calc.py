#!/usr/bin/python
'''
Every year, I play a March Madness pool where we pay out based on the last digits of the score.
This year, I am too busy to watch all the games or even keep track. So I created this to calculate
how much money I will win!

Sign up for API access @ https://www.kimonolabs.com/signup
'''
import json
import urllib
import pprint

# use your api-key
API_KEY = ""
# change the magic numbers to your win loss numbers.
MAGIC_NUMBERS = [{"w": 2, "l": 6}, 
                 {"w": 8, "l": 9}, 
                 {"w": 0, "l": 0}]

# Modify the payouts to what your pool pays out
PAYOUTS = {"Play-in": 0.0, "Round of 64": 2.5, "Round of 32": 5.0, "Round of 16": 10.0, "Round of 8": 20.0, "Round of 4": 40.0}

def calculate_win_loss(score1, score2):
    if score1 > score2:
        win = score1
        loss = score2
    else:
        win = score2
        loss = score1
    return win, loss

def main():
    games = json.load(urllib.urlopen("http://marchmadness.kimonolabs.com/api/games?tournamentGame=true&apikey=%s" % API_KEY))
    total_won = 0.0

    for each_game in games:
        win, loss = calculate_win_loss(each_game['homeScore'], each_game['awayScore'])
        for magic_number_set in MAGIC_NUMBERS:
            if magic_number_set['w'] == win % 10 and magic_number_set['l'] == loss % 10:
                game_round = each_game['tournamentGameInfo']['round']
                total_won += PAYOUTS[game_round]
                print "Score match in %s: %s - %s" % (game_round, each_game['homeTeamName'], each_game['awayTeamName']) 
    print "You have won a total of: $%.2f" % total_won

if __name__ == '__main__':
    main()
