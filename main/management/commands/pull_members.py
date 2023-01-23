import requests
from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import Members
from qp import settings


class Command(BaseCommand):
    help = 'pull members of Congress from the Congress API and saves them to the database'

    def handle(self, *args, **options):

        # max limit 250
        limit = 10

        response = requests.get(
            'https://api.congress.gov/v3/member',
            params={'api_key': settings.CONGRESS_API_KEY, 'format': 'json', 'limit': limit}
        )

        if response.status_code == 200:
            data = response.json()
            members = data['members']
            with transaction.atomic():
                for member in members:
                    member_obj = Members(bioguide_id=member.get('bioguideId', None),
                                         district=member.get('district', None),
                                         name=member.get('name', None),
                                         party=member.get('party', None),
                                         chamber=member.get('chamber', None),
                                         start_date=member.get('startDate', None),
                                         end_date=member.get('endDate', None),
                                         state=member.get('state', None),
                                         url=member.get('url', None))
                    member_obj.save()
        else:
            print(f'Error: {response.status_code}')

        print('Members imported successfully')
