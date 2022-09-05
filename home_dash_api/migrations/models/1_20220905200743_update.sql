-- upgrade --
CREATE TABLE IF NOT EXISTS "recipes" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "image" TEXT NOT NULL,
    "cooking_time" INT NOT NULL,
    "prep_time" INT NOT NULL,
    "servings" INT NOT NULL,
    "notes" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
CREATE TABLE IF NOT EXISTS "ingredient" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "ingredient_name" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
CREATE TABLE IF NOT EXISTS "measurement" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "measurement_name" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
CREATE TABLE IF NOT EXISTS "measurement_qty" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "measurement_qty_name" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
CREATE TABLE IF NOT EXISTS "recipe_ingredient" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "ingredient_id" UUID NOT NULL REFERENCES "ingredient" ("id") ON DELETE CASCADE,
    "measurement_id" UUID NOT NULL REFERENCES "measurement" ("id") ON DELETE CASCADE,
    "measurement_qty_id" UUID NOT NULL REFERENCES "measurement_qty" ("id") ON DELETE CASCADE,
    "recipe_id" UUID NOT NULL REFERENCES "recipes" ("id") ON DELETE CASCADE
);-- downgrade --
DROP TABLE IF EXISTS "recipes";
DROP TABLE IF EXISTS "ingredient";
DROP TABLE IF EXISTS "measurement";
DROP TABLE IF EXISTS "measurement_qty";
DROP TABLE IF EXISTS "recipe_ingredient";
