from tortoise import fields, models

class Recipe(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    image = fields.TextField()
    cooking_time = fields.IntField()
    prep_time = fields.IntField()
    servings = fields.IntField()
    notes = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "recipes"

    def __str__(self):
        return self.name
