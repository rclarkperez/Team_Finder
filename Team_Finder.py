import csv
import json
import requests

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def convert_to_snake_case(string):
    """Converts string input to snake case for use for print image function"""
    if not isinstance(string, str):
        print('not a string')
        return False
    words = string.strip().split()
    if not all(word.isalpha() for word in words):
        print('other')

        return False
    return '_'.join([word.capitalize() for word in words])


def print_image(team):
    """Full tram name used to find exact link to wikipedia logo for a given team"""
    if team == "Seattle_Seahawks":
        url = "https://upload.wikimedia.org/wikipedia/en/8/8e/Seattle_Seahawks_logo.svg"
        return url
    if team == "New_England_Patriots":
        url ="https://upload.wikimedia.org/wikipedia/en/b/b9/New_England_Patriots_logo.svg"
        return url

    if team == "Tampa_Bay_Buccaneers":
        url = "https://upload.wikimedia.org/wikipedia/en/a/a2/Tampa_Bay_Buccaneers_logo.svg"
        return url

    if team == "Indianapolis_Colts":
        url = "https://upload.wikimedia.org/wikipedia/commons/0/00/Indianapolis_Colts_logo.svg"
        return url

    if team == "Denver_Broncos":
        url = "https://upload.wikimedia.org/wikipedia/en/4/44/Denver_Broncos_logo.svg"
        return url

    if team == "Chicago_Bears":
        url = "https://upload.wikimedia.org/wikipedia/commons/5/5c/Chicago_Bears_logo.svg"
        return url

    if team == "New_Orleans_Saints":
        url = "https://upload.wikimedia.org/wikipedia/commons/5/50/New_Orleans_Saints_logo.svg"
        return url

    if team == "Carolina_Panthers":
        url = "https://upload.wikimedia.org/wikipedia/en/1/1c/Carolina_Panthers_logo.svg"
        return url

    if team == "Las_Vegas_Raiders":
        url = "https://upload.wikimedia.org/wikipedia/en/4/48/Las_Vegas_Raiders_logo.svg"
        return url

    if team == "Buffalo_Bills":
        url = "https://upload.wikimedia.org/wikipedia/en/7/77/Buffalo_Bills_logo.svg"
        return url

    if team == "Dallas_Cowboys":
        url = "https://upload.wikimedia.org/wikipedia/commons/1/15/Dallas_Cowboys.svg"
        return url

    if team == "Miami_Dolphins":
        url = "https://upload.wikimedia.org/wikipedia/en/3/37/Miami_Dolphins_logo.svg"
        return url

    if team == "Green_Bay_Packers":
        url = "https://upload.wikimedia.org/wikipedia/commons/5/50/Green_Bay_Packers_logo.svg"
        return url

    if team == "Arizona_Cardinals":
        url = "https://upload.wikimedia.org/wikipedia/en/7/72/Arizona_Cardinals_logo.svg"
        return url

    if team == "Washington_Commanders":
        "https://upload.wikimedia.org/wikipedia/commons/0/0c/Washington_Commanders_logo.svg"
        return url

    if team == "Cleveland_Browns":
        "https://upload.wikimedia.org/wikipedia/en/d/d9/Cleveland_Browns_logo.svg"
        return url

    if team == "San_Francisco_49ers":
        "https://upload.wikimedia.org/wikipedia/commons/3/3a/San_Francisco_49ers_logo.svg"
        return url

    if team == "Baltimore_Ravens":
        "https://upload.wikimedia.org/wikipedia/en/1/16/Baltimore_Ravens_logo.svg"
        return url

    if team == "Atlanta_Falcons":
        "https://upload.wikimedia.org/wikipedia/en/c/c5/Atlanta_Falcons_logo.svg"
        return url

    if team == "Tennessee_Titans":
        "https://upload.wikimedia.org/wikipedia/en/c/c1/Tennessee_Titans_logo.svg"
        return url

    if team == "Philadelphia_Eagles":
        "https://upload.wikimedia.org/wikipedia/en/8/8e/Philadelphia_Eagles_logo.svg"
        return url

    if team == "Cincinnati_Bengals":
        "https://upload.wikimedia.org/wikipedia/commons/8/81/Cincinnati_Bengals_logo.svg"
        return url

    if team == "Detroit_Lions":
        url = "https://upload.wikimedia.org/wikipedia/en/7/71/Detroit_Lions_logo.svg"
        return url

    if team == "Los_Angeles_Rams":
        url = "https://upload.wikimedia.org/wikipedia/en/8/8a/Los_Angeles_Rams_logo.svg"
        return url

    if team == "Houston_Texans":
        url = "https://upload.wikimedia.org/wikipedia/en/2/28/Houston_Texans_logo.svg"
        return url

    if team == "Jacksonville_Jaguars":
        url = "https://upload.wikimedia.org/wikipedia/en/7/74/Jacksonville_Jaguars_logo.svg"
        return url

    if team == "Kansas_City_Chiefs":
        url = "https://upload.wikimedia.org/wikipedia/en/e/e1/Kansas_City_Chiefs_logo.svg"
        return url

    if team == "Minnesota_Vikings":
        url = "https://upload.wikimedia.org/wikipedia/en/4/48/Minnesota_Vikings_logo.svg"
        return url

    if team == "Los_Angeles_Chargers":
        url = "https://upload.wikimedia.org/wikipedia/en/a/a6/Los_Angeles_Chargers_logo.svg"
        return url

    if team == "New_York_Giants":
        url = "https://upload.wikimedia.org/wikipedia/commons/6/60/New_York_Giants_logo.svg"
        return url

    if team == "New_York_Jets":
        url = "https://upload.wikimedia.org/wikipedia/en/6/6b/New_York_Jets_logo.svg"
        return url

    if team == "Pittsburgh_Steelers":
        url = "https://upload.wikimedia.org/wikipedia/commons/d/de/Pittsburgh_Steelers_logo.svg"
        return url
    else:
        return False


def logo_finder(region, team_name):
    """Takes region name and team name and returns link to logo of team"""
    team_name = convert_to_snake_case(team_name)
    region = convert_to_snake_case(region)
    print(team_name, region, 'team', 'region')
    # returns false if not entered
    if team_name is False or region is False:
        return "invalid input"
    full_name = f"{region}_{team_name}"
    print(full_name, "full name")
    return print_image(full_name)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

count = 0
while True:
    #  Wait for next request from client

    message = socket.recv()
    if count == 0:
        region_input = str(message)[1:].replace("'", "")
        '_'.join([word.capitalize() for word in region_input])
        print(region_input)
        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        socket.send(b"Please send team data")
        print(f"Received request: {message}")

        count += 1

    else:
        team_name_input = str(message)[1:].replace("'", "")
        '_'.join([word.capitalize() for word in team_name_input])
        print(team_name_input)
        #  Do some 'work'
        time.sleep(1)

        result = logo_finder(region_input, team_name_input)
        #  Send reply back to client
        socket.send_string(f'{result}')
        print(f"Received request: {message}")
