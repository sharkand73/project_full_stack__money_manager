DROP TABLE transactions;
DROP TABLE merchants;
DROP TABLE tags;
DROP TABLE budgets;

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
    date DATE,
    merchant_id int REFERENCES merchants(id) ON DELETE CASCADE,
    amount float,
    tag_id int REFERENCES tags(id) ON DELETE CASCADE
);

CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    start_date DATE,
    end_date DATE,
    amount FLOAT
)

