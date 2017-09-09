from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name = "姓氏")
    last_name = models.CharField(max_length=40, verbose_name = "名字")
    email = models.EmailField(blank = True, verbose_name = "邮箱")

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    def __str__(self):
        return self.__unicode__()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank = True, null = True)

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.__unicode__()
    

class User(models.Model):
    pass
