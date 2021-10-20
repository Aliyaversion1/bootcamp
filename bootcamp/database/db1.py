# aliya@aliya-GL552VX:~$ sudo -i -u postgres
# [sudo] password for aliya: 
# postgres@aliya-GL552VX:~$ psql postgres
# psql (12.8 (Ubuntu 12.8-0ubuntu0.20.04.1))
# Type "help" for help.

# postgres=# \l
# postgres=# \du
# postgres=# \l
#                                   List of databases
#    Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
# -----------+----------+----------+-------------+-------------+-----------------------
#  postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
#  template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
#            |          |          |             |             | postgres=CTc/postgres
#  template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
#            |          |          |             |             | postgres=CTc/postgres
# (3 rows)

# postgres=# create type condition as ENUM ('new', 'used', 'fixed');
# CREATE TYPE
# postgres=# create table car(
# postgres(# id serial primary key,
# postgres(# brand varchar(50) not null,
# postgres(# model varchar(50) not null,
# postgres(# state condition default 'new',
# postgres(# price money,
# postgres(# is_registered bool default true,
# postgres(# date_of_release date);
# CREATE TABLE
# postgres=# \dt
#         List of relations
#  Schema | Name | Type  |  Owner   
# --------+------+-------+----------
#  public | car  | table | postgres
# (1 row)

# postgres=# \d car
#                                         Table "public.car"
#      Column      |         Type          | Collation | Nullable |             Default             
# -----------------+-----------------------+-----------+----------+---------------------------------
#  id              | integer               |           | not null | nextval('car_id_seq'::regclass)
#  brand           | character varying(50) |           | not null | 
#  model           | character varying(50) |           | not null | 
#  state           | condition             |           |          | 'new'::condition
#  price           | money                 |           |          | 
#  is_registered   | boolean               |           |          | true
#  date_of_release | date                  |           |          | 
# Indexes:
#     "car_pkey" PRIMARY KEY, btree (id)

# postgres=# select * from car;
#  id | brand | model | state | price | is_registered | date_of_release 
# ----+-------+-------+-------+-------+---------------+-----------------
# (0 rows)
# postgres=# insert into car (brand, model, price, date_of_release) values ('toyota', 'camry 55', 31000, '2021/01/01');
# INSERT 0 1
# postgres=# select * from car;
#  id | brand  |  model   | state |     price     | is_registered | date_of_release 
# ----+--------+----------+-------+---------------+---------------+-----------------
#   1 | toyota | camry 55 | new   | 31 000.00 сом | t             | 2021-01-01
# (1 row)

# postgres=# insert into car (brand, model, price, date_of_release, state, is_registered) values ('BMW', 'X5', 25000, '2019/03/03', 'used', False);
# INSERT 0 1
# postgres=# insert into car (brand, model, price, date_of_release, state, is_registered) values ('Mercedes', '212', 34000, '2015/05/07', 'used', True);
# INSERT 0 1
# postgres=# select * from car;
#  id |  brand   |  model   | state |     price     | is_registered | date_of_release 
# ----+----------+----------+-------+---------------+---------------+-----------------
#   1 | toyota   | camry 55 | new   | 31 000.00 сом | t             | 2021-01-01
#   2 | BMW      | X5       | used  | 25 000.00 сом | f             | 2019-03-03
#   3 | Mercedes | 212      | used  | 34 000.00 сом | t             | 2015-05-07
# (3 rows)

# postgres=# insert into car (brand, model, price, date_of_release, state, is_registered) values ('Lexus', '505', 50000, '2021/05/07', 'new', false);
# INSERT 0 1
# postgres=# insert into car (brand, model, price, date_of_release, state, is_registered) values ('Lamborgini', '000', 360000, '2021/06/08', 'new', true);
# INSERT 0 1
# postgres=# select * from car;
#  id |   brand    |  model   | state |     price      | is_registered | date_of_release 
# ----+------------+----------+-------+----------------+---------------+-----------------
#   1 | toyota     | camry 55 | new   |  31 000.00 сом | t             | 2021-01-01
#   2 | BMW        | X5       | used  |  25 000.00 сом | f             | 2019-03-03
#   3 | Mercedes   | 212      | used  |  34 000.00 сом | t             | 2015-05-07
#   4 | Lexus      | 505      | new   |  50 000.00 сом | f             | 2021-05-07
#   5 | Lamborgini | 000      | new   | 360 000.00 сом | t             | 2021-06-08
# (5 rows)

# postgres=# select * from car where is_registered = true;
#  id |   brand    |  model   | state |     price      | is_registered | date_of_release 
# ----+------------+----------+-------+----------------+---------------+-----------------
#   1 | toyota     | camry 55 | new   |  31 000.00 сом | t             | 2021-01-01
#   3 | Mercedes   | 212      | used  |  34 000.00 сом | t             | 2015-05-07
#   5 | Lamborgini | 000      | new   | 360 000.00 сом | t             | 2021-06-08
# (3 rows)

# postgres=# select * from car where state = new;
# ERROR:  column "new" does not exist
# LINE 1: select * from car where state = new;
#                                         ^
# postgres=# select * from car where state = 'new';
#  id |   brand    |  model   | state |     price      | is_registered | date_of_release 
# ----+------------+----------+-------+----------------+---------------+-----------------
#   1 | toyota     | camry 55 | new   |  31 000.00 сом | t             | 2021-01-01
#   4 | Lexus      | 505      | new   |  50 000.00 сом | f             | 2021-05-07
#   5 | Lamborgini | 000      | new   | 360 000.00 сом | t             | 2021-06-08
# (3 rows)

# postgres=# \s

# postgres=# 
