from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from homes.models import House, Owner

class Command(BaseCommand):

  option_list = BaseCommand.option_list + (
    make_option('--addr_contains', action='store', type='string', help='add a new house by address'),
  )

  def handle(self, *args, **options):
    addrTerm = options['addr_contains']
    if addrTerm:
      houses = House.objects.getByAddrOrOwner(addrTerm)
      owners = House.objects.getHouseOwners(houses)
      for house in houses:
        self.stdout.write('Deleted house: id=[%d] address=[%s]' % (house.id, house.address) )
        for owner in owners:
          self.stdout.write(' Owner: name=[%s]' % (owner.name) )
        house.delete()
    else:
      raise CommandError('must specify the house address')
    for owner in owners:
      house = House.objects.all().filter(owner=owner)
      if not house:
        self.stdout.write('Deleted owner: id=[%d] name=[%s]' % (owner.id, owner.name) )
        owner.delete()
