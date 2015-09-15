from django.db import models, connection

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField('e-mail', blank=True)
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()

class MyBookManager(models.Manager):
    def get_queryset(self):
        return super(MyBookManager, self).get_queryset().filter(title__icontains="tantan")

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()
    my_objects = MyBookManager()
    def __str__(self):
        return self.title

class MaleManager(models.Manager):
    def get_queryset(self):
        return super(MaleManager, self).get_queryset().filter(sex='M')

class FemaleManager(models.Manager):
    def get_queryset(self):
        return super(FemaleManager, self).get_queryset().filter(sex='F')

class PersonManeger(models.Manager):
    def first_names(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT DISTINCT first_name FROM books_person
            WHERE last_name = %s""", [last_name])
        return [row[0] for row in cursor.fetchall()]

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=(('M','Male'), ('F','Female')))
    objects = PersonManeger()
    people = models.Manager()
    men = MaleManager()
    women = FemaleManager()
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)