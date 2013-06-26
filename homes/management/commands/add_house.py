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
      owner, newOwner = Owner.objects.getOrSave(ownerName)
      if newOwner:
        self.stdout.write('Added owner: id=[%d] name=[%s]' % (owner.id, owner.name) )
    else:
      raise CommandError('must specify the house owner')
    if houseAddr:
      house = House.objects.getOrSaveAndAdd(houseAddr, owner)
      if house:
        self.stdout.write('Added house: id=[%d] address=[%s] owner=[%s]' % (house.id, house.address, owner.name) )
      else:
        raise CommandError('that address already has an owner')
    else:
      raise CommandError('must specify the house address')
