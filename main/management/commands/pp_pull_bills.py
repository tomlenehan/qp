import os

from django.core.management import BaseCommand

from main.models import Bills
from django.utils import timezone
import requests


class Command(BaseCommand):
    help = 'pull data from propublica'

    def handle(self, *args, **options):
        api_key = os.getenv('PROPUBLICA_API_KEY')
        url = 'https://api.propublica.org/congress/v1'
        query_type = 'active'
        # query_type = 'introduced'
        congress = '118'

        for i in range(2):

            # if i == 0:
            #     chamber = 'house'
            # else:
            #     chamber = 'senate'

            chamber = 'both'
            query_type = 'passed'

            query = url+'/'+congress+'/'+chamber+'/bills/'+query_type+'.json'

            response = requests.get(query, headers={'X-API-Key': api_key})
            data = response.json()
            for bill in data['results'][0]['bills']:
                bill_obj, created = Bills.objects.update_or_create(
                    bill_id=bill['bill_id'],
                    defaults={
                        'bill_slug': bill.get('bill_slug'),
                        'bill_type': bill.get('bill_type'),
                        'number': bill.get('number'),
                        'bill_uri': bill.get('bill_uri'),
                        'title': bill.get('title'),
                        'short_title': bill.get('short_title'),
                        'sponsor_title': bill.get('sponsor_title'),
                        'sponsor_id': bill.get('sponsor_id'),
                        'sponsor_name': bill.get('sponsor_name'),
                        'sponsor_state': bill.get('sponsor_state'),
                        'sponsor_party': bill['sponsor_party'],
                        'sponsor_uri': bill['sponsor_uri'],
                        'gpo_pdf_uri': bill.get('gpo_pdf_uri'),
                        'congressdotgov_url': bill.get('congressdotgov_url'),
                        'govtrack_url': bill.get('govtrack_url'),
                        'introduced_date': bill.get('introduced_date'),
                        'active': bill.get('active'),
                        'last_vote': bill.get('last_vote'),
                        'house_passage': bill.get('house_passage'),
                        'senate_passage': bill.get('senate_passage'),
                        'enacted': bill.get('enacted'),
                        'vetoed': bill.get('vetoed'),
                        'cosponsors': bill.get('cosponsors'),
                        'cosponsors_by_party': bill.get('cosponsors_by_party'),
                        'committees': bill.get('committees'),
                        'committee_codes': bill.get('committee_codes'),
                        'subcommittee_codes': bill.get('subcommittee_codes'),
                        'primary_subject': bill.get('primary_subject'),
                        'summary': bill.get('summary'),
                        'summary_short': bill.get('summary_short'),
                        'latest_major_action_date': bill.get('latest_major_action_date'),
                        'latest_major_action': bill.get('latest_major_action')
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created bill {bill["title"]}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Successfully updated bill {bill["title"]}'))