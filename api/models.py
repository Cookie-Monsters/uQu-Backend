from django.db import models


class Question(models.Model):
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=6
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=6
    )


class User(models.Model):
    forename = models.CharField(
        max_length=50,
    )
    name = models.CharField(
        max_length=50,
    )
    email = models.EmailField()
    password = models.CharField(
        max_length=50,
    )


class Answer(models.Model):
    text = models.CharField(
        max_length=50,
    )
    image = models.ImageField(
        upload_to="/images"
    )
    type = models.CharField(
        max_length=50,
    )
    user = models.ForeignKey(
        User,
        db_column='User_id'
    )
    question = models.ForeignKey(
        Question,
        db_column='Question_id'
    )
