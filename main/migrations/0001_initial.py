# Generated by Django 4.1.5 on 2023-02-07 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillActions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=255)),
                ('action_date', models.DateField(blank=True, null=True)),
                ('action', models.TextField(blank=True, null=True)),
                ('chamber', models.CharField(blank=True, max_length=255, null=True)),
                ('congress', models.IntegerField(blank=True, null=True)),
                ('roll_call', models.IntegerField(blank=True, null=True)),
                ('result', models.CharField(blank=True, max_length=255, null=True)),
                ('vote_type', models.CharField(blank=True, max_length=255, null=True)),
                ('vote_question', models.TextField(blank=True, null=True)),
                ('vote_description', models.TextField(blank=True, null=True)),
                ('vote_required', models.CharField(blank=True, max_length=255, null=True)),
                ('passed', models.BooleanField(blank=True, null=True)),
                ('source_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=255, null=True, unique=True)),
                ('bill_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('bill_type', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(max_length=255, null=True)),
                ('bill_uri', models.URLField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('short_title', models.TextField(blank=True, null=True)),
                ('sponsor_title', models.CharField(blank=True, max_length=255, null=True)),
                ('sponsor_id', models.CharField(blank=True, max_length=255, null=True)),
                ('sponsor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sponsor_state', models.CharField(blank=True, max_length=255, null=True)),
                ('sponsor_party', models.CharField(blank=True, max_length=255, null=True)),
                ('sponsor_uri', models.URLField(blank=True, null=True)),
                ('gpo_pdf_uri', models.URLField(blank=True, null=True)),
                ('congressdotgov_url', models.URLField(blank=True, null=True)),
                ('govtrack_url', models.URLField(blank=True, null=True)),
                ('introduced_date', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('last_vote', models.DateField(blank=True, null=True)),
                ('house_passage', models.DateField(blank=True, null=True)),
                ('senate_passage', models.DateField(blank=True, null=True)),
                ('enacted', models.DateField(blank=True, null=True)),
                ('vetoed', models.DateField(blank=True, null=True)),
                ('cosponsors', models.IntegerField(blank=True, null=True)),
                ('cosponsors_by_party', models.JSONField(blank=True, null=True)),
                ('committees', models.TextField(blank=True, null=True)),
                ('committee_codes', models.JSONField(blank=True, null=True)),
                ('subcommittee_codes', models.JSONField(blank=True, null=True)),
                ('primary_subject', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('summary_short', models.TextField(blank=True, null=True)),
                ('latest_major_action_date', models.DateField(blank=True, null=True)),
                ('latest_major_action', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=25, unique=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('short_title', models.CharField(blank=True, max_length=255, null=True)),
                ('api_uri', models.URLField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('suffix', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('party', models.CharField(blank=True, max_length=10, null=True)),
                ('leadership_role', models.CharField(blank=True, max_length=50, null=True)),
                ('img_file', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_account', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_account', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_account', models.CharField(blank=True, max_length=255, null=True)),
                ('govtrack_id', models.CharField(blank=True, max_length=255, null=True)),
                ('cspan_id', models.CharField(blank=True, max_length=255, null=True)),
                ('votesmart_id', models.CharField(blank=True, max_length=255, null=True)),
                ('icpsr_id', models.CharField(blank=True, max_length=255, null=True)),
                ('crp_id', models.CharField(blank=True, max_length=255, null=True)),
                ('google_entity_id', models.CharField(blank=True, max_length=255, null=True)),
                ('fec_candidate_id', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('rss_url', models.URLField(blank=True, null=True)),
                ('contact_form', models.URLField(blank=True, null=True)),
                ('in_office', models.BooleanField(blank=True, null=True)),
                ('cook_pvi', models.FloatField(blank=True, null=True)),
                ('dw_nominate', models.FloatField(blank=True, null=True)),
                ('ideal_point', models.FloatField(blank=True, null=True)),
                ('seniority', models.CharField(blank=True, max_length=255, null=True)),
                ('next_election', models.CharField(blank=True, max_length=10, null=True)),
                ('total_votes', models.IntegerField(blank=True, null=True)),
                ('missed_votes', models.IntegerField(blank=True, null=True)),
                ('total_present', models.IntegerField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('ocd_id', models.CharField(blank=True, max_length=255, null=True)),
                ('office', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('fax', models.CharField(blank=True, max_length=25, null=True)),
                ('state', models.CharField(blank=True, max_length=25, null=True)),
                ('district', models.CharField(blank=True, max_length=25, null=True)),
                ('at_large', models.BooleanField(blank=True, null=True)),
                ('geoid', models.CharField(blank=True, max_length=25, null=True)),
                ('missed_votes_pct', models.FloatField(blank=True, null=True)),
                ('votes_with_party_pct', models.FloatField(blank=True, null=True)),
                ('votes_against_party_pct', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('statement_type', models.CharField(blank=True, max_length=255, null=True)),
                ('member_id', models.CharField(blank=True, max_length=255, null=True)),
                ('congress', models.IntegerField(blank=True, null=True)),
                ('member_uri', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('chamber', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('party', models.CharField(blank=True, max_length=255, null=True)),
                ('subjects', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingBills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(blank=True, max_length=12, null=True)),
                ('bill_slug', models.CharField(blank=True, max_length=10, null=True)),
                ('bill_type', models.CharField(blank=True, max_length=3, null=True)),
                ('bill_number', models.CharField(blank=True, max_length=10, null=True)),
                ('congress', models.CharField(blank=True, max_length=3, null=True)),
                ('chamber', models.CharField(blank=True, max_length=6, null=True)),
                ('api_uri', models.URLField(blank=True, null=True)),
                ('legislative_day', models.DateField(blank=True, null=True)),
                ('scheduled_at', models.DateTimeField(blank=True, null=True)),
                ('range', models.CharField(blank=True, max_length=5, null=True)),
                ('context', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('bill_url', models.URLField(blank=True, null=True)),
                ('consideration', models.CharField(blank=True, max_length=255, null=True)),
                ('source_type', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('congress', models.IntegerField(null=True)),
                ('chamber', models.CharField(max_length=6)),
                ('session', models.IntegerField(null=True)),
                ('roll_call', models.IntegerField(null=True)),
                ('source', models.URLField(null=True)),
                ('url', models.URLField(null=True)),
                ('vote_uri', models.URLField(null=True)),
                ('bill', models.TextField(null=True)),
                ('amendment', models.TextField(null=True)),
                ('question', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('vote_type', models.CharField(max_length=255, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('result', models.CharField(max_length=255)),
                ('democratic', models.TextField(null=True)),
                ('republican', models.TextField(null=True)),
                ('independent', models.TextField(null=True)),
                ('total', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillSponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bills')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.members')),
            ],
        ),
    ]
