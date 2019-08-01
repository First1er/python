from django.db import models

# Create your models here.

class joueur(models.Model):
	nom = models.CharField(max_length = 250)
	prenom = models.CharField(max_length = 250)
	email = models.CharField(max_length = 250)
	solde = models.IntegerField()
	mdpass = models.CharField(max_length = 250)

	#def __str__(self):
	#	return self.joueur_text

class equipe(models.Model):
	nom = models.CharField(max_length = 250)
	coach = models.CharField(max_length = 250)
	performance = models.IntegerField()

	#def __str__(self):
         #       return self.equipe_text


class ticket(models.Model):
	ref = models.CharField(max_length = 250)
	mise = models.IntegerField()
	gain = models.IntegerField() 

	#def __str__(self):
         #       return self.ticket_text
