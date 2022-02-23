create table player(
    id SERIAL PRIMARY KEY,
    ref_id char(9),
    full_name varchar(30),
    start_year integer,
    end_year integer,
    height_inches integer,
    weight_lbs integer,
    birth_date date
);

create table position(
    id SERIAL PRIMARY KEY,
    name varchar(15)
);

create table college(
    id SERIAL PRIMARY KEY,
    name varchar(30)
);