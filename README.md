# The Impact of the COVID-19 Pandemic on Bordering Discourses Regarding Migration and Mobility in Europe
## IT part

_More information about the project itself is available [here](https://nccr-onthemove.ch/projects/the-impact-of-the-covid-19-pandemic-on-bordering-discourses-regarding-migration-and-mobility-in-europe/)_

As of now, the goal is to regulargly scrape tweets from a list of international actors and constitute a database. This is done with the `src/scrape.py` script.

Tweets are classified as being about covid or not with a very basic keyword matching algorithm. See `src/common/classify.py`.

The process' pipeline is the following:
1. Scrape, classify and upload new tweets
2. Export the updated database to the `database/csv` folder
3. Convert the `.csv` file to `.xlsx` with the handy `convert-csv-to.xlsx` utils.
* `convert-csv-to-xlsx csv/tweets_all.csv xls/tweets_all.xlsx -d "," -e "utf-8"`

TODO:
- logging
- set up server
- ...
