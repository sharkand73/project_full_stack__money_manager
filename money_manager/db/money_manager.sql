DROP TABLE transactions;
DROP TABLE merchants;
DROP TABLE tags;

CREATE TABLE tags (
    category VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE merchants (
    name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id int REFERENCES merchants(id) ON DELETE CASCADE,
    amount float,
    tag_id int REFERENCES tags(id) ON DELETE CASCADE
);


