from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from homes.models import House, Owner

class Command(BaseCommand):

  option_list = BaseCommand.option_list + (
    make_option('--name', action='store', type='string', help='add a new owner'),
  )

  def handle(self, *args, **options):
    ownerName = options['name']
    owner, newOwner = Owner.objects.getOrSave(ownerName)
    if not newOwner:
      raise CommandError('an owner with name %s already exists' % ownerName)
    self.stdout.write('Added owner: id=[%d] name=[%s]' % (owner.id, owner.name))
