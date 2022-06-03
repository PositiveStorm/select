import sqlalchemy
from sqlalchemy import create_engine
from pprint import pprint
engine = sqlalchemy.create_engine('postgresql://polina1:555@localhost:5432/singeralbum')
engine
con = engine.connect()

pprint(con.execute(
    """
    
    SELECT name, year FROM album
    WHERE year = 2018
    
    """).fetchall())

pprint(con.execute(
    """

    SELECT name, duration FROM track
    WHERE duration = (SELECT MAX(duration) FROM track)

    """).fetchall())

pprint(con.execute(
    """

    SELECT name FROM track
    WHERE duration >= 0.90 

    """).fetchall())

pprint(con.execute(
    """

    SELECT name FROM collection
    WHERE year BETWEEN 2018 AND 2020 

    """).fetchall())

pprint(con.execute(
    """

    SELECT name FROM singer
    WHERE name NOT LIKE '%% %%'

    """).fetchall())

pprint(con.execute(
    """

    SELECT name FROM track
    WHERE name iLIKE '%%my%%'

    """).fetchall())