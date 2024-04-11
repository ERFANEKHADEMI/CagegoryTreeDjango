from django.db import models


class TreeCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    named_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name