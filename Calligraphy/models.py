from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    Form for user sign-up.

    Allows Django's UserCreationForm to include an email field.

    Attributes:
        email (forms.EmailField): A field for entering the user email.
    """
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        """
        Meta class for SignUpForm.

        Specifies the model and fields to be included in the form.
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CalligraphyStyle(models.Model):
    """
    Model for representing the Calligraphy styles.

    Attributes:
        name (models.CharField): Displays the name of the calligraphy styles.
        description (models.TextField()): Displays the description of each style.
    """
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()


class Artwork(models.Model):
    """
    Model class for displaying artwork of calligraphy.

    Attributes:
        title (models.CharField): The title of the artwork.
        style (models.ForeignKey): CalligraphyStyle associated with the artwork.
        artist (models.CharField): Artists name.
        image (models.ImageField): Image file of the artwork.
        uploaded_by (models.ForeignKey): The user who uploaded the artwork.
    """
    objects = None
    title = models.CharField(max_length=200)
    style = models.ForeignKey(CalligraphyStyle, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artwork_images/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    """
    returns a string representation of the artwork.

    Returns:
        str: The Title of the artwork.
    """
    return self.title
# Create your models here.
