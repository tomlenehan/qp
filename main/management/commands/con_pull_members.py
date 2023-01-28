import requests
from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import Members
from qp import settings


class Command(BaseCommand):
    help = 'pull members of Congress from the Congress API and saves them to the database'

    def handle(self, *args, **options):

        # Initialize variables
        offset = 0
        limit = 50
        member_count = 700

        while offset <= member_count:
            response = requests.get(
                'https://api.congress.gov/v3/member',
                params={'api_key': settings.CONGRESS_API_KEY, 'format': 'json', 'offset': offset, 'limit': limit}
            )

            if response.status_code == 200:
                data = response.json()
                members = data['members']
                with transaction.atomic():
                    for member in members:
                        chamber = list(member.get('served').keys())[0]
                        start = member.get('served').get(chamber)[0].get('start')
                        end = member.get('served').get(chamber)[0].get('end')

                        member_obj, created = Members.objects.get_or_create(
                            bioguide_id=member.get('bioguideId', None),
                            defaults={
                                'district': member.get('district', None),
                                'name': member.get('name', None),
                                'party': member.get('party', None),
                                'chamber': chamber,
                                'start_date': start,
                                'end_date': end,
                                'state': member.get('state', None),
                                'url': member.get('url', None),
                                'image_url': member.get('depiction').get('imageUrl')
                            }
                        )
                        if created:
                            member_obj.save()
                offset += limit
            else:
                print(f'Error: {response.status_code}')
        print('Members imported successfully')
