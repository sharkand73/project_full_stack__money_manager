-- This sql file was created in order to restore 
-- backup transactions during a phase in which I was
-- doing a lot of deleting of transactions, but also 
-- needed to have a month's worth of transactions handy.


-- DROP TABLE transactions;
-- DROP TABLE merchants;
-- DROP TABLE tags;
-- DROP TABLE budgets;
-- DROP TABLE testimonials;

-- CREATE TABLE tags as TABLE tags_backup;

-- CREATE TABLE merchants as TABLE merchants_backup;

-- CREATE TABLE transactions as TABLE transactions_backup;

-- CREATE TABLE budgets as TABLE budgets_backup;

-- CREATE TABLE testimonials (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     quote VARCHAR(255)
-- );


-- INSERT INTO testimonials (name, quote) VALUES ('Boaby, pure mad wi'' it, Ruchill', 'It''s bin pure amazin'' so it hus, a''ve definetly got mair money fur Buckie on a Wensday since a''ve did ma budget.'); 
-- INSERT INTO testimonials (name, quote) VALUES ('Ashraf, proprietor of Bammy Beverages', 'Sales are through the roof since my clients started using the app.');
-- INSERT INTO testimonials (name, quote) VALUES ('devShark''s mum', 'Whoever coded this deserves the Nobel Peace Prize');
-- INSERT INTO testimonials (name, quote) VALUES ('J. Caesar', 'Magnum opus!');
-- INSERT INTO testimonials (name, quote) VALUES ('Donald J. Trump', ' I don''t know this guy devShark, I never met him.');
-- INSERT INTO testimonials (name, quote) VALUES ('B. Gates', 'This kid has no future in tech.');
-- INSERT INTO testimonials (name, quote) VALUES ('S. Cowell', 'Worst CSS I''ve ever seen.');