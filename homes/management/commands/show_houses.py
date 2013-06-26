from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from homes.models import House, Owner

class Command(BaseCommand):

  option_list = BaseCommand.option_list + (
    make_option('--owner', action='store', type='string', help='show houses for an owner'),
    make_option('--addr_contains', action='store', type='string'),
  )

  def handle(self, *args, **options):
    ownerName, addrTerm = options['owner'], options['addr_contains']
    if ownerName:
      try:
        owner = Owner.objects.get(name=ownerName)
      except:
        raise CommandError('owner with name: %s does not exist' % ownerName)
      houses = House.objects.addrContainsOrOwner(addrTerm, owner)
    else:
      houses = House.objects.addrContainsOrAll(addrTerm)
    for house in houses:
      self.stdout.write('address=[%s] owner=[%s] id=[%d]' % (house.address, house.owner, house.id) )   
