import pandas as pd
import csv
import json
import ssl
import requests
ssl._create_default_https_context = ssl._create_unverified_context

def team_finder(first, last, plyr_year):
    """web-scrapes wikipedia for climate info on a given city. Data is returned in JSON format"""
    first = convert_to_snake_case(first)
    last = convert_to_snake_case(last)
    if first is False or last is False or plyr_year >2023 or plyr_year <2002:
        return "invalid input"
    url = f"https://en.wikipedia.org/wiki/{first}_{last}#Regular_season"
    try:
        html = pd.read_html(url, header=0)
    except Exception as e:
        return f"Error: {e}"
    df = html[6]
    save_team_csv(df, "team_report")
    return csv_to_json("team_report.csv", plyr_year)


def csv_to_json(file_name, plyr_year):
    """converts data in team data function from csv to json"""
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        columns = header[1:-1]

        data = {}
        for row in reader:
            category = row[0]
            values = row[1:-1]
            for i, value in enumerate(values):
                if columns[i] not in data:
                    data[columns[i]] = {}
                data[columns[i]][category] = value

        #print(data)
        try:
            data = data['Team'][f"{plyr_year}"]

            # Prints link to team logo of player
            print(print_image(data))

            if data == "SEA":
                team_name = "Seattle_Seahawks"
            if data == "NE":
                team_name = "New_England_Patriots"
            if data == "TB":
                team_name = "Tampa_Bay_Buccaneers"
            if data == "IND":
                team_name = "Indianapolis_Colts"
            if data == "DEN":
                team_name = "Denver_Broncos"
            if data == "CHI":
                team_name = "Chicago_Bears"
            if data == "NO":
                team_name = "New_Orleans_Saints"
            if data == "CAR":
                team_name = "Carolina_Panthers"
            if data == "LV":
                team_name = "Las_Vegas_Raiders"
            if data == "BUF":
                team_name = "Buffalo_Bills"
            if data == "DAL":
                team_name = "Dallas_Cowboys"
            if data == "MIA":
                team_name = "Miami_Dolphins"
            if data == "GB":
                team_name = "Green_Bay_Packers"
            if data == "ARI":
                team_name = "Arizona_Cardinals"
            if data == "WAS":
                team_name = "Washington_Commanders"
            if data == "CLE":
                team_name = "Cleveland_Browns"
            if data == "SF":
                team_name = "San_Francisco_49ers"
            if data == "BAL":
                team_name = "Baltimore_Ravens"
            if data == "ATL":
                team_name = "Atlanta_Falcons"
            if data == "TEN":
                team_name = "Tennessee_Titans"
            if data == "PHI":
                team_name = "Philadelphia_Eagles"
            if data == "CIN":
                team_name = "Cincinnati_Bengals"
            if data == "DET":
                team_name = "Detroit_Lions"
            if data == "LAR":
                team_name = "Los_Angeles_Rams"
            if data == "HOU":
                team_name = "Houston_Texans"
            if data == "JAX":
                team_name = "Jacksonville_Jaguars"
            if data == "KC":
                team_name = "Kansas_City_Chiefs"
            if data == "MIN":
                team_name = "Minnesota_Vikings"
            if data == "LAC":
                team_name = "Los_Angeles_Chargers"
            if data == "NYG":
                team_name = "New_York_Giants"
            if data == "NYJ":
                team_name = "New_York_Jets"
            if data == "JAX":
                team_name = "Jacksonville_Jaguars"
            if data == "PIT":
                team_name = "Pittsburgh_Steelers"
            return f"That player is from the {team_name}"
        except Exception as e:
            return "Invalid Year"


def save_team_csv(df, filename):
    """saves the team dataframe as a csv and removes unnecessary data"""
    df.to_csv(f"{filename}.csv")
    with open(f"{filename}.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = [row[1:] for row in csv_reader]
    with open(f"{filename}.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(rows[1:-1])


def convert_to_snake_case(string):
    """Converts string input to snake case for use in Wiki URL"""
    if not isinstance(string, str):
        return False
    words = string.strip().split()
    if not all(word.isalpha() for word in words):
        return False
    return '_'.join([word.capitalize() for word in words])

def get_image(url):
    """Gets image URL and returns text"""
    r = requests.get(url)
    return r.text

def print_image(team):
    """Team city acronym and returns link to team logo."""
    if team == "SEA":
        team_name = "Seattle_Seahawks"
    if team == "NE":
        team_name = "New_England_Patriots"
    if team == "TB":
        team_name = "Tampa_Bay_Buccaneers"
    if team == "IND":
        team_name = "Indianapolis_Colts"
    if team == "DEN":
        team_name = "Denver_Broncos"
    if team == "CHI":
        team_name = "Chicago_Bears"
    if team == "NO":
        team_name = "New_Orleans_Saints"
    if team == "CAR":
        team_name = "Carolina_Panthers"
    if team == "LV":
        team_name = "Las_Vegas_Raiders"
    if team == "BUF":
        team_name = "Buffalo_Bills"
    if team == "DAL":
        team_name = "Dallas_Cowboys"
    if team == "MIA":
        team_name = "Miami_Dolphins"
    if team == "GB":
        team_name = "Green_Bay_Packers"
    if team == "ARI":
        team_name = "Arizona_Cardinals"
    if team == "WAS":
        team_name = "Washington_Commanders"
    if team == "CLE":
        team_name = "Cleveland_Browns"
    if team == "SF":
        team_name = "San_Francisco_49ers"
    if team == "BAL":
        team_name = "Baltimore_Ravens"
    if team == "ATL":
        team_name = "Atlanta_Falcons"
    if team == "TEN":
        team_name = "Tennessee_Titans"
    if team == "PHI":
        team_name = "Philadelphia_Eagles"
    if team == "CIN":
        team_name = "Cincinnati_Bengals"
    if team == "DET":
        team_name = "Detroit_Lions"
    if team == "LAR":
        team_name = "Los_Angeles_Rams"
    if team == "HOU":
        team_name = "Houston_Texans"
    if team == "JAX":
        team_name = "Jacksonville_Jaguars"
    if team == "KC":
        team_name = "Kansas_City_Chiefs"
    if team == "MIN":
        team_name = "Minnesota_Vikings"
    if team == "LAC":
        team_name = "Los_Angeles_Chargers"
    if team == "NYG":
        team_name = "New_York_Giants"
    if team == "NYJ":
        team_name = "New_York_Jets"
    if team == "JAX":
        team_name = "Jacksonville_Jaguars"
    if team == "PIT":
        team_name = "Pittsburgh_Steelers"

    url = f"https://en.wikipedia.org/wiki/{team_name}#/media/File:{team_name}_logo.svg"
    return url


if __name__ == "__main__":
    # ex: print(team_finder("Peyton", "Manning", 2022))
