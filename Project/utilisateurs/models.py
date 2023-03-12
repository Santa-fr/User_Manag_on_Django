from django.db import models

class Utilisateur(models.Model):
    nom         = models.CharField(max_length=50)
    prenom      = models.CharField(max_length=20)
    mail        = models.EmailField()
    revues      = models.CharField(max_length=20)