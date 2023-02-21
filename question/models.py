from django.db import models

# Create your models here.
choices = (
    (1, "B.C.A. Ist"),
    (2, "B.C.A. 2nd"),
    (3, "B.C.A. 3rd"),
)


class AskMe(models.Model):
    name = models.CharField(max_length=20)
    student_class = models.IntegerField(choices=choices)
    student_email = models.EmailField()
    phone_number = models.IntegerField()
    question = models.TextField()

    def __str__(self):
        return self.name
