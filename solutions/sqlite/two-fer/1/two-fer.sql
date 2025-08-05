CREATE TABLE IF NOT EXISTS "twofer" (
    "input" TEXT,
    "response" TEXT
);
UPDATE twofer
SET response = 'One for ' ||
    CASE
        WHEN input = '' THEN 'you'
        ELSE input
    END ||
    ', one for me.';