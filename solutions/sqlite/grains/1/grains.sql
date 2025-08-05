-- Schema: CREATE TABLE "grains" ("task" TEXT, "square" INT, "result" INT);
UPDATE grains 
SET result =
  CASE
    WHEN task = "single-square" THEN POWER(2, square - 1)
    ELSE POWER(2, 64) - 1
  END