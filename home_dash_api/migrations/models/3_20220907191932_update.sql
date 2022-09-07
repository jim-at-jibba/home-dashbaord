-- upgrade --
CREATE TABLE IF NOT EXISTS "category" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "category_name" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
CREATE TABLE "recipe_categories" ("recipe_id" UUID NOT NULL REFERENCES "recipes" ("id") ON DELETE CASCADE,"category_id" UUID NOT NULL REFERENCES "category" ("id") ON DELETE CASCADE);
-- downgrade --
DROP TABLE IF EXISTS "recipe_categories";
DROP TABLE IF EXISTS "category";
