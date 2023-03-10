import os
import requests
from django.core.management import BaseCommand
from main.models import Members


# Attempt to get profile image from govtrack.us
def get_profile_image(member_id, govtrack_id):
    url = 'https://www.govtrack.us/static/legislator-photos/' + govtrack_id + '-200px.jpeg'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_name = member_id + '_200.jpg'
        file_path = 'frontend/static/images/profile_images/' + file_name
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return file_name
    else:
        return 'DEFAULT_200.jpg'


class Command(BaseCommand):
    help = 'pull data from propublica'

    def handle(self, *args, **options):
        api_key = os.getenv('PROPUBLICA_API_KEY')
        url = 'https://api.propublica.org/congress/v1/'
        query_type = 'active'
        congress_num = '118'

        for i in range(2):

            if i == 0:
                chamber = 'house'
            else:
                chamber = 'senate'

            query = url + congress_num + '/' + chamber + '/members.json'
            # query2 = "https://api.propublica.org/congress_num/v1/115/house/bills/introduced.json"

            response = requests.get(query, headers={'X-API-Key': api_key})
            data = response.json()
            for member in data['results'][0]['members']:

                # img_file = get_profile_image(member.get('id'), member.get('govtrack_id'))
                full_name = f"{member.get('first_name')} {member.get('last_name')}"

                member_obj, created = Members.objects.update_or_create(
                    member_id=member.get('id'),
                    defaults={
                        'title': member.get('title'),
                        'short_title': member.get('short_title'),
                        'api_uri': member.get('api_uri'),
                        'first_name': member.get('first_name'),
                        'middle_name': member.get('middle_name'),
                        'last_name': member.get('last_name'),
                        'full_name': full_name,
                        'suffix': member.get('suffix'),
                        'date_of_birth': member.get('date_of_birth'),
                        'gender': member.get('gender'),
                        'party': member.get('party'),
                        'leadership_role': member.get('leadership_role'),
                        # 'img_file': img_file,
                        'twitter_account': member.get('twitter_account'),
                        'facebook_account': member.get('facebook_account'),
                        'youtube_account': member.get('youtube_account'),
                        'govtrack_id': member.get('govtrack_id'),
                        'cspan_id': member.get('cspan_id'),
                        'votesmart_id': member.get('votesmart_id'),
                        'icpsr_id': member.get('icpsr_id'),
                        'crp_id': member.get('crp_id'),
                        'google_entity_id': member.get('google_entity_id'),
                        'fec_candidate_id': member.get('fec_candidate_id'),
                        'url': member.get('url'),
                        'rss_url': member.get('rss_url'),
                        'contact_form': member.get('contact_form'),
                        'in_office': member.get('in_office'),
                        'cook_pvi': member.get('cook_pvi'),
                        'dw_nominate': member.get('dw_nominate'),
                        'ideal_point': member.get('ideal_point'),
                        'seniority': member.get('seniority'),
                        'next_election': member.get('next_election'),
                        'total_votes': member.get('total_votes'),
                        'missed_votes': member.get('missed_votes'),
                        'total_present': member.get('total_present'),
                        'last_updated': member.get('last_updated'),
                        'ocd_id': member.get('ocd_id'),
                        'office': member.get('office'),
                        'phone': member.get('phone'),
                        'fax': member.get('fax'),
                        'state': member.get('state'),
                        'district': member.get('district'),
                        'at_large': member.get('at_large'),
                        'geoid': member.get('geoid'),
                        'missed_votes_pct': member.get('missed_votes_pct'),
                        'votes_with_party_pct': member.get('votes_with_party_pct'),
                        'votes_against_party_pct': member.get('votes_against_party_pct')
                    }
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Successfully created member {member["first_name"]} {member["last_name"]}'))
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f'Successfully updated member {member["first_name"]} {member["last_name"]}'))
