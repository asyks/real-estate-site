from django.db import models

# models for homes app: homes owners

class Owner(models.Model):

  name = models.TextField(unique=True) 

  def __unicode__(self):
    return self.name

class House(models.Model):

  address = models.TextField(unique=True)
  owner = models.OneToOneField(Owner)

  def __unicode__(self):
    return self.name
