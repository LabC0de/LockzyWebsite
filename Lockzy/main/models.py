from django.db import models


# Create your models here.
class ContentTable(models.Model):
    title = models.CharField(max_length=128, default="TITLE")
    path_to_related_links_html = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Article(models.Model):
    belongs_to = models.ForeignKey(ContentTable, on_delete=models.CASCADE)
    link_text = models.CharField(max_length=128, default="NONE")
    url_additum = models.CharField(max_length=256)

    def __str__(self):
        return self.link_text


class Order(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    served = models.BooleanField(default=False)

