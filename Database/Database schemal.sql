-- create table 1: auborncountry
CREATE TABLE auborncountry(
    index INT PRIMARY KEY,
    countryname VARCHAR,
    population_2021_thousands DECIMAL,
    population_2021_percentage DECIMAL)
    
-- create table 2: countryorigin
CREATE TABLE countryorigin(
    index INT PRIMARY KEY,
    countryname VARCHAR,
    visitor_est_in_2022_thousands DECIMAL)
    
-- create table 3: countrydestination
CREATE TABLE countrydestination(
    index INT PRIMARY KEY,
    countryname VARCHAR,
    visitor_est_out_2021_thousands DECIMAL)
