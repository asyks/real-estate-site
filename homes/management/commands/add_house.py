from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from homes.models import House, Owner

class Command(BaseCommand):

  option_list = BaseCommand.option_list + (
    make_option('--address', action='store', type='string', help='add a new house by address'),
    make_option('--owner', action='store', type='string', help='add a new house by owner and address'),
  )

  def handle(self, *args, **options):
    houseAddr, ownerName = options['address'], options['owner']
    if ownerName:
      try:
        owner = Owner.objects.get(name=ownerName)
      except:
        owner = Owner(name=ownerName)
        owner.save()
        owner = Owner.objects.get(name=ownerName)
        self.stdout.write('Added owner: name=[%s] id=[%d]' % (owner.name, owner.id) )
    else:
      raise CommandError('must specify the house owner')
    if houseAddr:
      house = House(address=houseAddr, owner=owner)
      house.save()
      self.stdout.write('Added house: address=[%s] owner=[%s] id=[%d]' % (house.address, house.owner, house.id) )
    else:
      raise CommandError('must specify the house address')
