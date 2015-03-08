import os 
import csv
import random
from academy.models import Invite
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):

	def handle(self, *args, **options):
		print "Loading CSV"
		Invite.objects.all().delete()
		csv_path = os.path.join(settings.BASE_DIR, "academy_invites_2014.csv")

		csv_file = open(csv_path, 'rb')
		csv_obj = csv.DictReader(csv_file)
		for row in csv_obj:
			reporter= random.choice(['Clark Kent', 'Lois Lane'])
			Invite.objects.create(
				name=row['Name'],
				branch=row['Branch'],
				reporter = reporter
				)
				
				
				