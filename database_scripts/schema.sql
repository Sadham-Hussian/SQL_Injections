DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;

CREATE TABLE users (
  id serial PRIMARY KEY,
  username varchar(30) UNIQUE NOT NULL,
  password text NOT NULL,
  type text NOT NULL
);

CREATE TABLE products (
  id serial PRIMARY KEY,
  name varchar(30) UNIQUE NOT NULL,
  price text NOT NULL,
  quantity text NOT NULL
);