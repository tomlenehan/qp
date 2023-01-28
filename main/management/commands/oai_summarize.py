import openai
import requests
from django.core.management.base import BaseCommand

from qp import settings


class Command(BaseCommand):
    help = 'Uses OpenAI to summarize text from a URL and put it in layman\'s terms'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='The URL to summarize')

    def handle(self, *args, **options):
        # openai API key
        openai.api_key = settings.OPENAI_API_KEY

        # Make a request to the URL
        text = requests.get(options['url']).text

        # Use the OpenAI API to summarize the text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=(f"summarize the following text in layman's terms: {text}")
        )

        # Print the summary
        summary = response["choices"][0]["text"]
        print(summary)
