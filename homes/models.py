from django.db import models

# models for homes app: homes owners

class OwnerManager(models.Manager):

  def getOrSave(self, ownerName):
    try:
      owner = Owner.objects.get(name=ownerName)
      newOwner = False
    except:
      owner = Owner(name=ownerName)
      owner.save()
      owner = Owner.objects.get(name=ownerName) 
      newOwner = True
    return owner, newOwner

class Owner(models.Model):

  name = models.TextField(unique=True) 

  objects = OwnerManager()

  def __unicode__(self):
    return self.name

class HouseManager(models.Manager):

  def addrContainsOrOwner(self, addrTerm, owner):
    if addrTerm:
      houses = House.objects.all().filter(address__contains=addrTerm, owner=owner)
    else:
      houses = House.objects.all().filter(owner=owner)
    return houses

  def addrContainsOrAll(self, addrTerm):
    if addrTerm:
      houses = House.objects.all().filter(address__contains=addrTerm)
    else:
      houses = House.objects.all()
    return houses

class House(models.Model):

  address = models.TextField(unique=True)
  owner = models.OneToOneField(Owner)

  objects = HouseManager()

  def __unicode__(self):
    return self.name
