load data local infile 'c:\\pemba\\csv\\57_maintenance.csv' into table maintenance
    ->  fields terminated by ','
    ->  enclosed by '"'
    ->  lines terminated by '\n'
    ->  ignore 1 rows;