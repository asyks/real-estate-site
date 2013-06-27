from django.db import models

## models for homes app: House, Owner 

## Owner model manager object for use with both OneToOne
## and ManyToMany relationship
class OwnerManager(models.Manager):

  def getOrSave(self, ownerName):
    try:
      owner = Owner.objects.get(name=ownerName)
      newOwner = False
    except:
      owner = Owner(name=ownerName)
      owner.save()
      newOwner = True
    return owner, newOwner

## Owner model for homes app
class Owner(models.Model):

  name = models.TextField(unique=True) 

  objects = OwnerManager()

  def __unicode__(self):
    return self.name

## House model manager object for use with OneToOne relationship
class HouseManagerOneToOne(models.Manager):

  def getByAddrOrOwner(self, addrTerm=None, owner=None):
    if owner:
      if addrTerm:
        houses = House.objects.all().filter(address__contains=addrTerm, owner=owner)
      else:
        houses = House.objects.all().filter(owner=owner)
    else:
      if addrTerm:
        houses = House.objects.all().filter(address__contains=addrTerm)
      else:
        houses = House.objects.all()
      return houses

  def getOrSaveAndAdd(self, houseAddr, owner):
    house = House(address=houseAddr, owner=owner)
    house.save()
    return house

  def getHouseOwners(self, houses):
    owners = []
    for house in houses:
      owners.append(house.owner)
    return owners

## House model manager object for use with ManyToMany relationship
class HouseManagerManyToMany(HouseManagerOneToOne):

  def getOrSaveAndAdd(self, houseAddr, owner):
    try:
      house = House.objects.get(address=houseAddr)
    except:
      house = House(address=houseAddr)
      house.save()
    house.owner.add(owner)
    return house

  def getHouseOwners(self, houses):
    owners = []
    for house in houses:
      for owner in house.owner.all():
        owners.append(owner)
    return owners

## House model for homes app
class House(models.Model):

  address = models.TextField(unique=True)
  owner = models.ManyToManyField(Owner)
  ## uncomment the line below and comment out the line above to switch back to
  ## a One to One relationship between Houses and Owners
  # owner = models.OneToOneField(Owner)

  objects = HouseManagerManyToMany()
  ## uncomment the line below and comment out the line above to switch back to
  ## switch between ManyToMany and OneToOne model.Manager
  # objects = HouseManagerOneToOne()

  def __unicode__(self):
    return self.address
