"""
Converter module
"""

import csv
from datetime import date

import openpyxl

from common.database import Database


class Converter:
    """
    Convert database table to csv
    """

    def __init__(self, database: Database, mode: str):
        self.database = database
        self.mode = mode

    def convert_by_columns(
        self,
        cols: tuple = (
            "tweet_id",
            "covid_theme",
            "created_at",
            "handle",
            "name",
            "oldtext",
            "text",
            "url",
            "type",
            "retweets",
            "favorites",
        ),
    ):
        """
        Convert tweets table to csv by columns
        """

        today = str(date.today())

        outfile = self.database.db_name
        outfile = outfile.strip(".db")

        with self.database, open(
            f"database/csv/{outfile}-{today}.csv", "w+", encoding="utf-8", newline=""
        ) as out:
            try:
                writer = csv.writer(out, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow(cols)
                tweets = self.database.get_fields(list(cols))
                writer.writerows(tweets)
                print(
                    f"Table successfully converted as database/csv/{outfile}-{today}.csv"
                )

                return f"{outfile}-{today}.csv"
            except csv.Error as error:
                print("Error while writing CSV", error)

    def csv_to_xlsx(self, csv_file):
        """
        Export a csv file to xlsx
        """

        workbook = openpyxl.Workbook()
        sheet = workbook.active

        with open(f"database/csv/{csv_file}", "r", encoding="utf8", newline="") as file:
            reader = csv.reader(file)
            for row_i, row in enumerate(reader, start=1):
                for col_i, val in enumerate(row, start=1):
                    sheet.cell(row=row_i, column=col_i).value = val
        try:
            csv_file = csv_file.strip(".csv")
            workbook.save(f"database/xlsx/{csv_file}.xlsx")
            print(f"File successfully exported to database/xlsx/{csv_file}.xlsx")
        except openpyxl.utils.exceptions.InvalidFileException as error:
            print("Error", error)
