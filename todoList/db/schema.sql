-- create DATABASE todos;
\c todos michelle;
DROP TABLE IF EXISTS todo ;
CREATE TABLE todo (
    id SERIAL,
    title TEXT,
    createTime TIMESTAMP DEFAULT current_timestamp,
    primary key (id)
);

