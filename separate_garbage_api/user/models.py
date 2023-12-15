import uuid
from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    draft = models.BooleanField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        super(User, self).save(*args, **kwargs)