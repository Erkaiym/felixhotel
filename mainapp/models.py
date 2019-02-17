from django.core.exceptions import ValidationError
from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    comment = models.TextField()
    image = models.ImageField(blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.company}'


class Recommendation(models.Model):
    company_name = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.company_name


class Certificate(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title


class AboutCompany(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name = 'About company'
        verbose_name_plural = 'About company'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if AboutCompany.objects.exists() and not self.pk:
            raise ValidationError('There is can be only one About Company instance')
        return super(AboutCompany, self).save(*args, **kwargs)
