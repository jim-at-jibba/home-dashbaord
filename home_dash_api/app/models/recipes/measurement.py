from tortoise import fields, models


class Measurement(models.Model):
    id = fields.UUIDField(pk=True)
    measurement_name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "measurement"

    class PydanticMeta:
        exclude = ("created_at", "updated_at")

    def __str__(self):
        return self.measurement_name
