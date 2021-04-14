DROP TABLE transactions;
DROP TABLE merchants;
DROP TABLE tags;
DROP TABLE budgets;
DROP TABLE plugin_transactions;
DROP TABLE testimonials;

CREATE TABLE tags (
    category VARCHAR(255) UNIQUE,
    id SERIAL PRIMARY KEY
);

CREATE TABLE merchants (
    name VARCHAR(255) UNIQUE,
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
    name VARCHAR(255),
    start_date DATE,
    end_date DATE,
    amount FLOAT
);

CREATE TABLE plugin_transactions (
    id SERIAL PRIMARY KEY,
    date DATE,
    merchant_name VARCHAR(255),
    amount float,
    tag_category VARCHAR(255)
);

CREATE TABLE testimonials (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    quote VARCHAR(255)
);


INSERT INTO merchants (name) VALUES ('Tesco');
INSERT INTO tags (category) VALUES ('Groceries');
-- INSERT INTO budgets (name,start_date,end_date,amount) VALUES ('March 2021','2021-03-01', '2021-03-01', 1100);

INSERT INTO testimonials (name, quote) VALUES ('Boaby, pure mad wi'' it, Ruchill', 'It''s bin pure amazin'' so it hus, a''ve definetly got mair money fur Buckie on a Wensday since a''ve did ma budget.'); 
INSERT INTO testimonials (name, quote) VALUES ('Ashraf, proprietor of Bammy Beverages', 'Sales are through the roof since my clients started using the app.');
INSERT INTO testimonials (name, quote) VALUES ('devShark''s mum', 'Whoever coded this deserves the Nobel Peace Prize');
INSERT INTO testimonials (name, quote) VALUES ('J. Caesar', 'Magnum opus!');
INSERT INTO testimonials (name, quote) VALUES ('Donald J. Trump', ' I don''t know this guy devShark, I never met him.');
INSERT INTO testimonials (name, quote) VALUES ('B. Gates', 'This kid has no future in tech.');
INSERT INTO testimonials (name, quote) VALUES ('S. Cowell', 'Worst CSS I''ve ever seen.');