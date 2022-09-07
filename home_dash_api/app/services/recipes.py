from app.models.recipes.category import Category
from app.models.recipes.ingredient import Ingredient
from app.models.recipes.measurement import Measurement
from app.models.recipes.measurement_qty import MeasurementQty
from app.models.recipes.recipe import Recipe
from app.models.recipes.recipe_ingredients import RecipeIngredient
from app.schemas.recipes import CreateRecipe, RecipeSchema
from app.schemas.user import UserSchema
from tortoise.contrib.pydantic.creator import pydantic_queryset_creator
from tortoise.query_utils import Prefetch


async def create_recipe(recipe: CreateRecipe, user: UserSchema) -> Recipe:
    recipe = Recipe(
        name=recipe.name,
        description=recipe.description,
        image=recipe.image,
        cooking_time=recipe.cooking_time,
        prep_time=recipe.prep_time,
        servings=recipe.servings,
        notes=recipe.notes,
        creator=user,
    )

    await recipe.save()
    return recipe


async def create_recipe_ingredient(
    recipe: Recipe,
    ingredient: Ingredient,
    measurement: Measurement,
    measurement_qty: MeasurementQty,
):
    print(recipe.id, ingredient.id, measurement_qty.id, measurement.id)
    recipe_ingredient = RecipeIngredient(
        recipe=recipe,
        ingredient=ingredient,
        measurement=measurement,
        measurement_qty=measurement_qty,
    )

    await recipe_ingredient.save()


async def create_ingredient(ingredient_name: str) -> Ingredient:
    db_ingredient = await Ingredient.filter(ingredient_name=ingredient_name).first()
    if not db_ingredient:
        ingredient = Ingredient(
            ingredient_name=ingredient_name,
        )

        await ingredient.save()
        return ingredient
    return db_ingredient


async def create_measurement(measurement_name: str) -> Measurement:
    db_measurement = await Measurement.filter(measurement_name=measurement_name).first()
    if not db_measurement:
        measurement = Measurement(
            measurement_name=measurement_name,
        )

        await measurement.save()
        return measurement
    return db_measurement


async def create_measurement_qty(mq: str) -> MeasurementQty:
    db_measurement_qty = await MeasurementQty.filter(measurement_qty_name=mq).first()
    if not db_measurement_qty:
        measurement_qty = MeasurementQty(measurement_qty_name=mq)

        await measurement_qty.save()
        return measurement_qty
    return db_measurement_qty


async def create_category(category_name: str) -> Category:
    db_category = await Category.filter(category_name=category_name).first()
    if not db_category:
        category = Category(
            category_name=category_name,
        )

        await category.save()
        return category

    return db_category


async def create_recipe_transaction(recipe: CreateRecipe, user: UserSchema):
    db_recipe = await create_recipe(recipe, user)
    cats = []
    for category in recipe.categories:
        cat = await create_category(category.category_name)
        cats.append(cat)

    await db_recipe.categories.add(*cats)

    for ingredient in recipe.ingredients:
        db_ingredient = await create_ingredient(
            ingredient_name=ingredient.ingredient_name
        )
        measurement = await create_measurement(measurement_name=ingredient.measurement)
        measurement_qty = await create_measurement_qty(mq=ingredient.measurement_qty)
        await create_recipe_ingredient(
            recipe=db_recipe,
            ingredient=db_ingredient,
            measurement=measurement,
            measurement_qty=measurement_qty,
        )

    return recipe


async def get_recipes_s():
    recipes = Recipe.all()
    Recipe_List = pydantic_queryset_creator(Recipe)
    return await Recipe_List.from_queryset(recipes)
