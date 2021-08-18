from django.db import models

SURNAME= {
    ('Mrs.','Mrs.'),
    ('Mr.','Mr.'),
    ('Ms','Ms'),
}

class Profiles(models.Model):
    title = models.CharField(max_length=30, choices=SURNAME)
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.CharField(max_length=60, default="", blank=True, null=False)
    username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_name