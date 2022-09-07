from app.schemas.recipes import CreateRecipe
from app.schemas.user import UserSchema
from app.services.recipes import create_recipe_transaction, get_recipes_s
from app.services.user import get_current_user, get_user_by_email
from fastapi import APIRouter, Depends, HTTPException

recipe_router = APIRouter()


@recipe_router.post("/api/recipes")
async def recipe_create(
    recipe: CreateRecipe, user: UserSchema = Depends(get_current_user)
):
    db_user = await get_user_by_email(user.email)

    recipe = await create_recipe_transaction(recipe, user=db_user)


@recipe_router.get("/api/recipes")
async def get_recipes(user: UserSchema = Depends(get_current_user)):
    db_user = await get_user_by_email(user.email)
    print(db_user)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    recipes = await get_recipes_s()
    return recipes
