<p align="center">
    <img alt="Zlogo" src="https://i.ytimg.com/vi/QhSOVD74oRI/maxresdefault.jpg" />
</p>
<h1 align="center">
    NBA APP ALGORITHM
</h1>

searches through NBA player heights
based on user input. The raw data is taken from
[here](https://www.openintro.org/data/index.php?data=nba_heights).  The data is
served in json format by the endpoint
[here](https://mach-eight.uc.r.appspot.com/).

The task is to create an application that takes a single integer input. The
application will download the raw data from the website above
(https://mach-eight.uc.r.appspot.com) and print a list of all pairs of players
whose height in inches adds up to the integer input to the application. If no
matches are found, the application will print "No matches found"

# Prerequisites

* `python` => v3.8.5
* `requests`==2.25.1

# Installation
* `git clone https://github.com/Giraluna1/NBA_players_app.git`
* `cd nba_players/`

# Running
The program has a file that stores data for testing is filestorage.json because the the web endpoint can change the data.
The program has two work environments:
* for run the app type: `NBA_ENV=dev python3 core/NBA_players_app.py [integer that is the sum of two heights]`
* for run the test enviroment type: `NBA_ENV=test python3 -m unittest discover tests`

# Example
input:

`NBA_ENV=dev python3 core/NBA_players_app.py 139`

Output:
```
-Mike Wilks    Nate Robinson
-Brevin Knight    Nate Robinson

```
input:

`NBA_ENV=dev python3 core/NBA_players_app.py 100`

Output:
```
No matches found
```

The test enviroment

input:

`NBA_ENV=test python3 -m unittest discover tests`

output:
```
-Mike Wilks    Nate Robinson
-Brevin Knight    Nate Robinson
.No matches found
.-Chucky Atkins    Nate Robinson
-Brevin Knight    Mike Wilks
-Nate Robinson    Speedy Claxton
.-Yao Ming    Zydrunas Ilgauskas
-Yao Ming    Zydrunas Ilgauskas
.
----------------------------------------------------------------------
Ran 4 tests in 0.012s

OK
```
# Authors
<div align='center'>
  <div>
    <table>
      <tr>
        <td valign="top" align='center'>
            <a href="https://github.com/Giraluna1" target="_blank">
            <p>Giraluna Gomez</p>
            <img alt="github_page" src="https://avatars.githubusercontent.com/u/70671381?v=4" height="80" width="80" />
            </a>
            <br />
            <a href="https://www.linkedin.com/in/giralunagomez/" target="_blank" rel="noopener noreferrer">
            <img src="https://img.icons8.com/plasticine/100/000000/linkedin.png" width="35" />
            </a>
            <a href="https://twitter.com/luna_gom" target="_blank" rel="noopener noreferrer">
            <img src="https://img.icons8.com/plasticine/100/000000/twitter.png" width="35" />
            </a>
        </td>