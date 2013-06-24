from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from homes.models import House, Owner

class Command(BaseCommand):

  option_list = BaseCommand.option_list + (
    make_option('--name', action='store', type='string', help='add a new owner'),
  )

  def handle(self, *args, **options):
    ownerName = options['name']
    try:
      owner = Owner(name=ownerName)
      owner.save()
    except:
      raise CommandError('an owner with name %s already exists' % ownerName)
    owner = Owner.objects.get(name=ownerName)
    self.stdout.write('Added owner: name=[%s] id=[%d]' % (owner.name, owner.id))
