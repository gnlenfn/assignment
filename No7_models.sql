-- create tables
create table person(
	person_id integer primary key not null,
	year_of_birth integer,
	month_of_birth integer,
	day_of_birth integer,
	gender_value char(50),
	race_value char(50),
	ethnicity_value char(50)
);

create table visit_occurrence(
	visit_occurrence_id integer primary key not null,
    person_id integer,
    foreign key (person_id)
    references person(person_id) on update cascade,
	visit_start_date date,
	care_site_nm text,
	visit_type_value char(50)
);

create table drug_exposure(
	drug_exposure_id integer primary key not null,
	person_id integer,
	foreign key (person_id)
	references person(person_id) on update cascade,
	drug_exposure_start_date date,
	drug_value text,
	route_value char(50),
	dose_value char(50),
	unit_value char(50),
	visit_occurrence_id integer,
	foreign key (visit_occurrence_id)
	references visit_occurrence(visit_occurrence_id) on update cascade
);

create table condition_occurrence(
	condition_occurrence_id integer primary key not null,
	person_id integer,
	foreign key (person_id)
	references person(person_id) on update cascade,
	condition_start_date date,
	condition_value text,
	visit_occurrence_id integer,
	foreign key (visit_occurrence_id)
	references visit_occurrence(visit_occurrence_id) on update cascade
);