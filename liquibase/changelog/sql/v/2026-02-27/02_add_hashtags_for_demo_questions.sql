--liquibase formatted sql

--changeset m.kroll:13
--comment: Add hashtags for new demo questions

INSERT INTO hashtags (name) VALUES
('Belief'),
('Burnout'),
('Cinematography'),
('Empathy'),
('Experience'),
('FastFashion'),
('Gentrifcation'),
('Glamping'),
('Happiness'),
('LifeGoals'),
('Mindfulness'),
('MOBA'),
('Analog'),
('Piercings'),
('Responsibility'),
('Scam'),
('Situationships'),
('Trends'),
('Wealth'),
('WorkPlace'),
('Schizophrenia'),
('Order'),
('Meaning'),
('Body'),
('Event'),
('Academic')
ON CONFLICT (name) DO NOTHING;
