-- create table 1: auborncountry
CREATE TABLE auborncountry(
    countryname VARCHAR PRIMARY KEY,
    population_2021_thousands DECIMAL,
    population_2021_percentage DECIMAL);
    
-- create table 2: countryorigin
CREATE TABLE countryorigin(
    countryname VARCHAR PRIMARY KEY,
    visitor_est_in_2022_thousands DECIMAL);
    
-- create table 3: countrydestination
CREATE TABLE countrydestination(
    countryname VARCHAR PRIMARY KEY,
    visitor_est_out_2021_thousands DECIMAL);
