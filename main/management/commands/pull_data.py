import os

from django.core.management import BaseCommand

from main.models import Bill
from django.utils import timezone
import requests


class Command(BaseCommand):
    help = 'pull data from propublica'

    def handle(self, *args, **options):
        api_key = os.getenv('PROPUBLICA_API_KEY')
        response = requests.get(f'https://api.propublica.org/congress/v1/116/senate/bills/introduced.json',
                                headers={'X-API-Key': api_key})
        data = response.json()
        for bill in data['results'][0]['bills']:
            bill_obj, created = Bill.objects.update_or_create(
                bill_id=bill['bill_id'],
                defaults={
                    'bill_uri': bill['bill_uri'],
                    'title': bill['title'],
                    'sponsor_id': bill['sponsor_id'],
                    'sponsor_uri': bill['sponsor_uri'],
                    'sponsor_name': bill['sponsor_name'],
                    'sponsor_party': bill['sponsor_party'],
                    'sponsor_state': bill['sponsor_state'],
                    'introduced_date': bill['introduced_date'],
                    'latest_major_action_date': bill['latest_major_action_date'],
                    'latest_major_action': bill['latest_major_action'],
                    'committees': bill['committees'],
                    'cosponsors': bill['cosponsors'],
                    'cosponsors_count': bill.get('cosponsors_count', 0),
                    'primary_subject': bill['primary_subject'],
                    'summary': bill['summary'],
                    'summary_short': bill['summary_short'],
                    'updated_at': timezone.now(),
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created bill {bill["bill_id"]}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated bill {bill["bill_id"]}'))
