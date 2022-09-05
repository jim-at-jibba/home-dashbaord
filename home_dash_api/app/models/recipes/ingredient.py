from tortoise import fields, models

class Ingredient(models.Model):
    id = fields.UUIDField(pk=True)
    ingredient_name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "ingredient"

    def __str__(self):
        return self.ingredient_name
