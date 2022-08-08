"""API models file."""
# Django
from django.db import models

# Python

class Character(models.Model):
    """Fictional character model class.
    
    Table to identify and save characters from tv series, movies
    animes, and other visual media.

    Fields:
    - name: A character name
    - appears_in: character's series comes from
    """
    name = models.CharField(max_length=100)
    appears_in = models.CharField(max_length=100)

    def __str__(self):
        """Returns a string with the character name."""
        return str(self.name)
