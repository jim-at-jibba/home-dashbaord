-- upgrade --
ALTER TABLE "recipes" ADD "creator_id" UUID NOT NULL;
ALTER TABLE "recipes" ADD CONSTRAINT "fk_recipes_users_800b3600" FOREIGN KEY ("creator_id") REFERENCES "users" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "recipes" DROP CONSTRAINT "fk_recipes_users_800b3600";
ALTER TABLE "recipes" DROP COLUMN "creator_id";
