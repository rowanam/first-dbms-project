from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# define class-based model for "City" table
class City(base):
    __tablename__ = "City"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    population = Column(Integer, primary_key=False)


# instead of connecting the the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# ---------- CREATE ----------

# create instances of "Place"
london = City(
    name="London",
    country="UK",
    population=8982000
)

berlin = City(
    name="Berlin",
    country="Germany",
    population=3645000
)

perth = City(
    name="Perth",
    country="Australia",
    population=1985000
)

bangkok = City(
    name="Bangkok",
    country="Thailand",
    population=10723000
)

fes = City(
    name="Fes",
    country="Morocco",
    population=1290000
)

# session.add(london)
# session.add(berlin)
# session.add(perth)
# session.add(bangkok)
# session.add(fes)

# session.commit()


# ---------- READ ----------

# view city populations
# cities = session.query(City)
# for city in cities:
#     print(city.name, "population: ", city.population)

# get cities with population over 2 million
# biggest_cities = session.query(City).filter(City.population > 2000000)
# print("Cities with population over 2 million:")
# for city in biggest_cities:
#     print(city.name)


# ---------- UPDATE ----------

# add a city with wrong population info
paris = City(
    name="Paris",
    country="France",
    population=1000000
)
# session.add(paris)
# session.commit()

# update paris population info
# paris_entry = session.query(City).filter_by(name="Paris").first()
# paris_entry.population = 2161000
# session.commit()

# change UK to United Kingdom
# uk_cities = session.query(City).filter_by(country="UK")
# for city in uk_cities:
#     city.country = "United Kingdom"
#     session.commit()


# ---------- DELETE ----------

# delete Paris record
# city = session.query(City).filter_by(name="Paris").first()
# session.delete(city)
# session.commit()


# ---------- VIEW FULL TABLE ----------

# query all records in "City" table
cities = session.query(City)
for city in cities:
    print(city.id, city.name, city.country, city.population, sep=" | ")
