from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # Used to generate urls by reversing the URL patterns
from django.db.models.signals import post_save
#relation containg all genre of books



##relation containing language of books




class Book(models.Model):
    title = models.CharField('Titre',max_length=200)
    author = models.CharField('Auteur',max_length=100)
    summary = models.TextField('sommaire',max_length=1000, help_text="Enter une description pour le livre")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    total_copies = models.IntegerField('total copies')
    available_copies = models.IntegerField('copy disponible')
    pic=models.ImageField('Image',blank=True, null=True, upload_to='book_image')

#return canonical url for an object
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    ##  __str__ method is used to override default string returnd by an object
    def __str__(self):
        return self.title


def create_user(sender, *args, **kwargs):
    if kwargs['created']:
        user = User.objects.create(username=kwargs['instance'],password="dummypass")

#memoire models

class Memoire(models.Model):

    title = models.CharField('Titre',max_length=200)
    student = models.CharField('student',max_length=100)
    summary = models.TextField('Résumé',max_length=1000)
    def get_absolute_url(self):
        return reverse('memoire-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


#relation containing info about students

class Student(models.Model):
    roll_no = models.CharField('Id_etud',max_length=10,unique=True)
    name = models.CharField('Nom',max_length=10)
    branch = models.CharField('Niveau',max_length=3)
    contact_no = models.CharField('Contact',max_length=10)
    total_books_due=models.IntegerField('Total livres',default=0)
    email=models.EmailField('email',unique=True)
    pic=models.ImageField('image',blank=True, upload_to='profile_image')
    def __str__(self):
        return str(self.roll_no)


post_save.connect(create_user, sender=Student)
#relation containing info about Borrowed books
#it has  foriegn key book and student for refrencing book nad student
#roll_no is used for identifing students
#if a book is returned than corresponding tuple is deleted from database
class Borrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.student.name+" borrowed "+self.book.title




