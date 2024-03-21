from django.db import models

class Filme(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, default='')
    palavras = models.TextField()
    def __str__(self):
        return f"{self.title}"
    
class FunFacts(models.Model):
    fact = models.TextField()
    def __str__(self) -> str:
        return f"{self.id}. {self.fact}"
    
class Anuncio(models.Model):
    headline = models.TextField(max_length=200)
    img = models.URLField(max_length=200)
    link = models.URLField(max_length=200)
    def __str__(self) -> str:
        return f'{self.id}. {self.headline}'