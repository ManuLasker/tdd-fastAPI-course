from tortoise import fields, models


class TextSummary(models.Model):
    # Creating a text summary model using tortoise models.Model meta class
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.url
