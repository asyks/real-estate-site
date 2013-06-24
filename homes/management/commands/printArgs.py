from django.core.management.base import BaseCommand, CommandError
from homes.models import House, Owner

class Command(BaseCommand):

  args = ''
  help = ''

  def handle(self, *args, **options):
#    self.stdout.write(args)
    print args
