import json
import lxml
import operator
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.request import urlopen

STAT_COUNT = 8

players = [
    {
        "name": "Steven Wright",
        "id": 453214,
        "pitches": []
    },
    {
        "name": "Jason Marquis",
        "id": 150302,
        "pitches": []
    },
    {
        "name": "Anthony DeSclafani",
        "id": 543101,
        "pitches": []
    },
    {
        "name": "Masahiro Tanaka",
        "id": 547888,
        "pitches": []
    },
    {
        "name": "Michael Pineda",
        "id": 501381,
        "pitches": []
    },
    {
        "name": "CC Sabathia",
        "id": 282332,
        "pitches": []
    },
    {
        "name": "Bud Norris",
        "id": 502032,
        "pitches": []
    },
    {
        "name": "Ubaldo Jimenez",
        "id": 434622,
        "pitches": []
    },
    {
        "name": "Chris Tillman",
        "id": 501957,
        "pitches": []
    },
    {
        "name": "Jake Odorizzi",
        "id": 543606,
        "pitches": []
    },
    {
        "name": "Matt Andriese",
        "id": 542882,
        "pitches": []
    },
    {
        "name": "Erasmo Ramirez",
        "id": 285063,
        "pitches": []
    },
    {
        "name": "Chris Archer",
        "id": 502042,
        "pitches": []
    },
    {
        "name": "Julio Teheran",
        "id": 527054,
        "pitches": []
    },
    {
        "name": "Alex Wood",
        "id": 622072,
        "pitches": []
    },
    {
        "name": "Shelby Miller",
        "id": 571946,
        "pitches": []
    },
    {
        "name": "Drew Smyly",
        "id": 592767,
        "pitches": []
    },
    {
        "name": "Joe Kelly",
        "id": 523260,
        "pitches": []
    },
    {
        "name": "Clay Buchholz",
        "id": 453329,
        "pitches": []
    },
    {
        "name": "Rick Porcello",
        "id": 519144,
        "pitches": []
    },
    {
        "name": "Carlos Carrasco",
        "id": 471911,
        "pitches": []
    },
    {
        "name": "Corey Kluber",
        "id": 446372,
        "pitches": []
    },
    {
        "name": "Trevor Bauer",
        "id": 545333,
        "pitches": []
    },
    {
        "name": "Chase Whitley",
        "id": 595032,
        "pitches": []
    },
    {
        "name": "Wade Miley",
        "id": 489119,
        "pitches": []
    },
    {
        "name": "Miguel Gonzalez",
        "id": 456068,
        "pitches": []
    },
    {
        "name": "Roberto Hernandez",
        "id": 433584,
        "pitches": []
    },
    {
        "name": "Dallas Keuchel",
        "id": 572971,
        "pitches": []
    },
    {
        "name": "Scott Feldman",
        "id": 444857,
        "pitches": []
    },
    {
        "name": "Collin McHugh",
        "id": 543521,
        "pitches": []
    },
    {
        "name": "C.J. Wilson",
        "id": 450351,
        "pitches": []
    },
    {
        "name": "Hector Santiago",
        "id": 502327,
        "pitches": []
    },
    {
        "name": "Jered Weaver",
        "id": 450308,
        "pitches": []
    },
    {
        "name": "Matt Shoemaker",
        "id": 533167,
        "pitches": []
    },
    {
        "name": "Felix Hernandez",
        "id": 433587,
        "pitches": []
    },
    {
        "name": "James Paxton",
        "id": 572020,
        "pitches": []
    },
    {
        "name": "Taijuan Walker",
        "id": 592836,
        "pitches": []
    },
    {
        "name": "Hector Noesi",
        "id": 456051,
        "pitches": []
    },
    {
        "name": "John Danks",
        "id": 433579,
        "pitches": []
    },
    {
        "name": "Jeff Samardzija",
        "id": 502188,
        "pitches": []
    },
    {
        "name": "Trevor May",
        "id": 543507,
        "pitches": []
    },
    {
        "name": "Kyle Gibson",
        "id": 502043,
        "pitches": []
    },
    {
        "name": "Ricky Nolasco",
        "id": 445060,
        "pitches": []
    },
    {
        "name": "Jordan Zimmermann",
        "id": 519455,
        "pitches": []
    },
    {
        "name": "Max Scherzer",
        "id": 453286,
        "pitches": []
    },
    {
        "name": "Taylor Jordan",
        "id": 518863,
        "pitches": []
    },
    {
        "name": "Brett Oberholtzer",
        "id": 519085,
        "pitches": []
    },
    {
        "name": "Brad Hand",
        "id": 543272,
        "pitches": []
    },
    {
        "name": "Dan Haren",
        "id": 429717,
        "pitches": []
    },
    {
        "name": "Tom Koehler",
        "id": 543408,
        "pitches": []
    },
    {
        "name": "Eduardo Rodriguez",
        "id": 593958,
        "pitches": []
    },
    {
        "name": "Noah Syndergaard",
        "id": 592789,
        "pitches": []
    },
    {
        "name": "Matt Harvey",
        "id": 518774,
        "pitches": []
    },
    {
        "name": "Jonathon Niese",
        "id": 477003,
        "pitches": []
    },
    {
        "name": "Bartolo Colon",
        "id": 112526,
        "pitches": []
    },
    {
        "name": "Mike Wright",
        "id": 605541,
        "pitches": []
    },
    {
        "name": "Kevin Gausman",
        "id": 592332,
        "pitches": []
    },
    {
        "name": "Nathan Karns",
        "id": 501992,
        "pitches": []
    },
    {
        "name": "Nick Martinez",
        "id": 607259,
        "pitches": []
    },
    {
        "name": "Yovani Gallardo",
        "id": 451596,
        "pitches": []
    },
    {
        "name": "Chi Chi Gonzalez",
        "id": 592346,
        "pitches": []
    },
    {
        "name": "Anibal Sanchez",
        "id": 434671,
        "pitches": []
    },
    {
        "name": "Justin Verlander",
        "id": 434378,
        "pitches": []
    },
    {
        "name": "Chris Sale",
        "id": 519242,
        "pitches": []
    },
    {
        "name": "Jose Quintana",
        "id": 500779,
        "pitches": []
    },
    {
        "name": "Danny Duffy",
        "id": 518633,
        "pitches": []
    },
    {
        "name": "Chris Young",
        "id": 432934,
        "pitches": []
    },
    {
        "name": "Edinson Volquez",
        "id": 450172,
        "pitches": []
    },
    {
        "name": "Kendall Graveman",
        "id": 608665,
        "pitches": []
    },
    {
        "name": "Sonny Gray",
        "id": 543243,
        "pitches": []
    },
    {
        "name": "Drew Pomeranz",
        "id": 519141,
        "pitches": []
    },
    {
        "name": "J.A. Happ",
        "id": 457918,
        "pitches": []
    },
    {
        "name": "Adam Morgan",
        "id": 605388,
        "pitches": []
    },
    {
        "name": "Jerome Williams",
        "id": 425532,
        "pitches": []
    },
    {
        "name": "Johnny Cueto",
        "id": 456501,
        "pitches": []
    },
    {
        "name": "Yordano Ventura",
        "id": 570649,
        "pitches": []
    },
    {
        "name": "Ervin Santana",
        "id": 429722,
        "pitches": []
    },
    {
        "name": "Phil Hughes",
        "id": 461833,
        "pitches": []
    },
    {
        "name": "Tyler Duffey",
        "id": 608648,
        "pitches": []
    },
    {
        "name": "Nathan Eovaldi",
        "id": 543135,
        "pitches": []
    },
    {
        "name": "Ivan Nova",
        "id": 467100,
        "pitches": []
    },
    {
        "name": "Aaron Brooks",
        "id": 605156,
        "pitches": []
    },
    {
        "name": "Jesse Chavez",
        "id": 445926,
        "pitches": []
    },
    {
        "name": "Luis Severino",
        "id": 622663,
        "pitches": []
    },
    {
        "name": "Aaron Nola",
        "id": 605400,
        "pitches": []
    },
    {
        "name": "Andrew Heaney",
        "id": 571760,
        "pitches": []
    },
    {
        "name": "Garrett Richards",
        "id": 572070,
        "pitches": []
    },
    {
        "name": "Derek Holland",
        "id": 502706,
        "pitches": []
    },
    {
        "name": "Colby Lewis",
        "id": 407890,
        "pitches": []
    },
    {
        "name": "Buck Farmer",
        "id": 571656,
        "pitches": []
    },
    {
        "name": "Alfredo Simon",
        "id": 430580,
        "pitches": []
    },
    {
        "name": "Danny Salazar",
        "id": 517593,
        "pitches": []
    },
    {
        "name": "Cody Anderson",
        "id": 594736,
        "pitches": []
    },
    {
        "name": "Henry Owens",
        "id": 596064,
        "pitches": []
    },
    {
        "name": "Matt Wisler",
        "id": 605538,
        "pitches": []
    },
    {
        "name": "Rich Hill",
        "id": 448179,
        "pitches": []
    },
    {
        "name": "Adam Warren",
        "id": 476589,
        "pitches": []
    },
    {
        "name": "Tyler Wilson",
        "id": 592869,
        "pitches": []
    },
    {
        "name": "Matt Moore",
        "id": 519043,
        "pitches": []
    },
    {
        "name": "Cole Hamels",
        "id": 430935,
        "pitches": []
    },
    {
        "name": "Martin Perez",
        "id": 527048,
        "pitches": []
    }
]

for player in players:
    season_url = "http://www.brooksbaseball.net/tabs.php?player={}&p_hand=-1&ppos=-1&cn=200&compType=none&risp=0&1b=0&2b=0&3b=0&rType=perc&time=month&minmax=ci&var=traj&s_type=2&startDate=04/01/2015&endDate=05/01/2015&gFilt=allmlb".format(player["id"])

    data = urlopen(season_url)
    soup = BeautifulSoup(data, "lxml")
    data = soup.find("table")

    stats = data.findAll("td")

    for stat in range(0, len(stats)):
        stats[stat] = re.sub("<.*?>", "", str(stats[stat]))

    for stat in range(0, len(stats), STAT_COUNT):
        player["pitches"].append(stats[stat:stat+STAT_COUNT])

def obj_dict(obj):
    return obj.__dict__

with open("april_pitchers_data.json", "w") as outputfile:
    json.dump(players, outputfile, default=obj_dict)
