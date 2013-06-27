from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from homes.models import House, Owner

class Command(BaseCommand):

  def handle(self, *args, **options):
    owners = Owner.objects.all()
    for owner in owners:
      self.stdout.write('Owner: id=[%d] name=[%s]' % (owner.id, owner.name))
      for house in owner.house_set.all():
        self.stdout.write(' House: id=[%d] address=[%s]' % (house.id, house.address))
        
