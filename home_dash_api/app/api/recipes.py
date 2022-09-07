from app.schemas.recipes import CreateRecipe
from app.schemas.user import UserSchema
from app.services.recipes import create_recipe_transaction
from app.services.user import get_current_user, get_user_by_email
from fastapi import APIRouter, Depends, HTTPException

recipe_router = APIRouter()


@recipe_router.post("/api/recipe")
async def recipe_create(
    recipe: CreateRecipe, user: UserSchema = Depends(get_current_user)
):
    db_user = await get_user_by_email(user.email)

    recipe = await create_recipe_transaction(recipe, user=db_user)
