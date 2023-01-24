import requests
from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Bills
from qp import settings


class Command(BaseCommand):
    help = 'Pull bills from the Congress API and save to the database'

    def handle(self, *args, **options):

        # max limit 250
        limit = 10

        response = requests.get(
            'https://api.congress.gov/v3/bill',
            params={'api_key': settings.CONGRESS_API_KEY, 'format': 'json', 'limit': limit}
        )

        if response.status_code == 200:
            data = response.json()
            bills = data['bills']
            with transaction.atomic():
                for bill in bills:
                    bill_obj = Bills(
                        number=bill['number'],
                        title=bill['title'],
                        type=bill['type'],
                        congress=bill['congress'],
                        latest_action_date=bill['latestAction']['actionDate'],
                        latest_action_text=bill['latestAction']['text'],
                        origin_chamber=bill['originChamber'],
                        origin_chamber_code=bill['originChamberCode'],
                        update_date=bill['updateDate'],
                        url=bill['url']
                    )
                    bill_obj.save()
        else:
            print(f'Error: {response.status_code}')
