from tortoise import fields, models


class Category(models.Model):
    id = fields.UUIDField(pk=True)
    recipes = fields.ManyToManyField(
        "models.Recipe", related_name="categories", through="recipe_categories"
    )
    category_name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "category"

    def __str__(self):
        return self.category_name
