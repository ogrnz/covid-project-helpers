"""
Database module
"""

import sqlite3


class Database:
    """
    Class that handles database queries
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def connect(self):
        """
        Establish connection to database
        """

        try:
            self.conn = sqlite3.connect(f'database/{self.db_name}')
        except sqlite3.Error as error:
            print(
                f'Error establishing connection to database {self.db_name}\n', error)

    def create_table(self, table_sql):
        """
        Create an SQL table
        """
        try:
            cur = self.conn.cursor()
            cur.execute(table_sql)
        except sqlite3.Error as error:
            print('Error creating table', error)

    def get_by_type(self, tweet_type: str):
        """
        Retrieve tweets by type
        :param type: available types are ['Retweet','New', 'Reply']
        """

        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM tweets WHERE type=?", (tweet_type,))

            return cur.fetchall()
        except sqlite3.Error as error:
            print('Error', error)
        finally:
            cur.close()

    def update_tweet_by_id(self, tweet_id: int, field: str, content: any):
        """
        Update tweet in database by id
        """

        sql = f'''UPDATE tweets
             SET {field} = ?
             WHERE tweet_id = ?'''
        cur = self.conn.cursor()

        try:
            cur.execute(sql, (content, tweet_id,))
            self.conn.commit()
        except sqlite3.Error as error:
            print(f'Error updating tweet {tweet_id} ', error)
        finally:
            cur.close()

    def insert_tweet(self, tweet):
        """
        Insert new tweet into database
        """
        sql = ''' INSERT OR IGNORE INTO tweets(
                        tweet_id,
                        covid_theme,
                        type, 
                        created_at, 
                        handle, 
                        name, 
                        oldtext,
                        text,
                        url,
                        retweets,
                        favorites)
                VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
        cur = self.conn.cursor()

        try:
            cur.execute(sql, tweet)
            self.conn.commit()

            return cur.lastrowid
        except sqlite3.Error as error:
            print(f'Error inserting new tweet \n {tweet} \n {error}')
        finally:
            cur.close()

    def get_last_id_by_handle(self, screen_name):
        """
        Retrieve last inserted tweet id in database for a given
        username
        """

        screen_name = f'@{screen_name}'
        cur = self.conn.cursor()

        try:
            cur.execute('''
                SELECT tweet_id 
                FROM tweets 
                WHERE handle=?
                ORDER BY tweet_id DESC''',
                        (screen_name,)
                        )

            return cur.fetchone()
        except sqlite3.Error as error:
            print(f'Error retrieving last tweet in db for {screen_name}\
                    \n {error}')
        finally:
            cur.close()


if __name__ == "__main__":

    db = Database('tweets_tests.db')

    # print(len(db.get_by_type('Reply')))

    # db.update_tweet_by_id(1341331429100294144, 'text', None)
    # #id doesn't exist, why no error raised?

    # tweet = (123, 0, 'New', '19/02/2021 17:00:01', '@Fake', 'Fake', \
    #          None, 'tweet', 'google.com', 0, 100)
    # db.insert_tweet(tweet)

    # print(db.get_last_id_by_handle('EU_Commission'))

    # del db