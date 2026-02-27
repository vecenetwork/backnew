--liquibase formatted sql

--changeset m.kroll:4

CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    subscriber_id INT NOT NULL,
    subscribed_to_id INT NOT NULL,
    subscribed_to_type VARCHAR(10) CHECK (subscribed_to_type IN ('user', 'hashtag')),
    favourite BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),

    CONSTRAINT fk_subscriber FOREIGN KEY (subscriber_id) REFERENCES users(id) ON DELETE CASCADE,
    -- `subscribed_to_id` can reference either `users` or `hashtags`, so no direct FK constraint here.
    CONSTRAINT unique_subscription UNIQUE (subscriber_id, subscribed_to_id, subscribed_to_type)
);

CREATE INDEX idx_subscriber_id ON subscriptions (subscriber_id);
CREATE INDEX idx_subscribed_to_id ON subscriptions (subscribed_to_id);
CREATE INDEX idx_subscriber_type ON subscriptions (subscriber_id, subscribed_to_type);
CREATE INDEX idx_subscribed_to_type ON subscriptions (subscribed_to_id, subscribed_to_type);
