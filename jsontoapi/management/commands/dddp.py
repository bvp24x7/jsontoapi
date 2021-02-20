from django.core.management.base import BaseCommand, CommandError
from jsontoapi.models import *
import json
import dateutil.parser as parser

f = open('/home/prasad/Documents/toyapp/ftl/jsontoapi/TestJSON.json','r')

output = json.load(f)
print(output) 

class Command(BaseCommand):
    help = 'Json loading'

    # def add_arguments(self, parser):
    #     parser.add_argument( nargs='+', type=int)

    def handle(self, *args, **options):
  

        # from pathlib import Path

        # BASE_DIR = Path(__file__).resolve().parent.parent
        # print(BASE_DIR/'TestJSON.json')
        for member in output['members']:
            print(member['id'])
            User1.objects.create(id=member['id'],real_name = member['real_name'], tz=member['tz'])
            user = User1.objects.get(id=member['id'])
            
            for times in member['activity_periods']:
                starttime = times['start_time']
                start_date = parser.parse(starttime)
                formated_start = start_date.isoformat()

                endtime = times['end_time']
                end_date = parser.parse(endtime)
                formated_end = end_date.isoformat()
                
                Activity_periods.objects.create(user = user, start_time = formated_start, end_time = formated_end)


        self.stdout.write(self.style.SUCCESS('Successfully closed poll '))