

CREATE TABLE data_type (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(45),
  summary VARCHAR(512),
  description TEXT
);


-- INSERT 3 records

INSERT INTO data_type (
  name,
  summary,
  description
) VALUES (
  "Integers",
  "Integer values",
  "A data type that allows us to stores integer values"
);

INSERT INTO data_type (
  name,
  summary,
  description
) VALUES (
  "Float",
  "Floating point values",
  "A data type that allows us to store multiple values after the decimal point"
);

INSERT INTO data_type (
  name,
  summary,
  description
) VALUES (
  "Booleans",
  "True or false values",
  "Named after George Boole (Boolean algebra); These can take True or False as their values"
);
