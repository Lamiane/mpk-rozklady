# MPK Rozkłady

This script downloads schedules from [MPK](http://www.mpk.krakow.pl/) site, parses them and saves as a csv.

## Installation
Will need:
* pandas
* numpy
* urlllib

## Usage
Copy the urls with timetables of interest into the `linki.txt` file (one url per line). There cannot be multiple links with the schedule of the same line.

Run `python run.py`, the schedules will be saved to `rozklady.csv`.

Sample `linki.txt` and generated `rozklady.csv` are provided. Have fun.
