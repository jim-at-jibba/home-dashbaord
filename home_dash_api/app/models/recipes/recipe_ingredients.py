from app.models.recipes.ingredient import Ingredient
from app.models.recipes.measurement import Measurement
from app.models.recipes.measurement_qty import MeasurementQty
from app.models.recipes.recipe import Recipe
from tortoise import Tortoise, fields, models


class RecipeIngredient(models.Model):
    recipe: fields.ForeignKeyRelation["Recipe"] = fields.ForeignKeyField(
        "models.Recipe"
    )
    ingredient: fields.ForeignKeyRelation["Ingredient"] = fields.ForeignKeyField(
        "models.Ingredient"
    )
    measurement: fields.ForeignKeyRelation["Measurement"] = fields.ForeignKeyField(
        "models.Measurement"
    )
    measurement_qty: fields.ForeignKeyRelation[
        "MeasurementQty"
    ] = fields.ForeignKeyField("models.MeasurementQty")

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "recipe_ingredient"
