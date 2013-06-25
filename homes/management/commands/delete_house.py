from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from homes.models import House, Owner

class Command(BaseCommand):

  option_list = BaseCommand.option_list + (
    make_option('--addr_contains', action='store', type='string', help='add a new house by address'),
  )

  def handle(self, *args, **options):
    addrTerm, owners = options['addr_contains'], []
    if addrTerm:
      houses = House.objects.all().filter(address__contains=addrTerm)
      for house in houses:
        owners.append(house.owner)
        self.stdout.write('Deleted house: address=[%s] owner=[%s] id=[%d]' % (house.address, house.owner, house.id) )
        house.delete()
    else:
      raise CommandError('must specify the house address')
    for owner in owners:
      house = House.objects.all().filter(owner=owner)
      if not house:
        self.stdout.write('Deleted owner: name=[%s] id=[%d]' % (owner.name, owner.id) )
        owner.delete()

## should delete house delete more than one house?
