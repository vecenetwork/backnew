--liquibase formatted sql

--changeset m.kroll:12
--comment: Add show_country, show_gender, show_age to user_settings for filter visibility in profile

ALTER TABLE user_settings ADD COLUMN IF NOT EXISTS show_country BOOLEAN DEFAULT TRUE;
ALTER TABLE user_settings ADD COLUMN IF NOT EXISTS show_gender BOOLEAN DEFAULT TRUE;
ALTER TABLE user_settings ADD COLUMN IF NOT EXISTS show_age BOOLEAN DEFAULT TRUE;
