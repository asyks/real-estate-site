from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from homes.models import House, Owner

class Command(BaseCommand):

  option_list = BaseCommand.option_list + (
    make_option('--owner', action='store', type='string', help='show houses for an owner'),
  )

  def handle(self, *args, **options):
    ownerName = options['owner']
    if ownerName:
      try:
        owner = Owner.objects.get(name=ownerName)
        houses = House.objects.all().filter(owner=owner)
      except:
        raise CommandError('owner with name: %s dose not exist' % ownerName)
    else:
      houses = House.objects.all()
    for house in houses:
      self.stdout.write('address=[%s] owner=[%s]' % (house.address, house.owner) )   
