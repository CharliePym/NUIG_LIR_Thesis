# Generated by Django 4.2.2 on 2023-06-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judgments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judgment_id', models.BigIntegerField(blank=True, null=True)),
                ('neutral_citation', models.TextField(blank=True, null=True)),
                ('judgment_title', models.TextField(blank=True, null=True)),
                ('judgment_date', models.TextField(blank=True, null=True)),
                ('court_name', models.TextField(blank=True, null=True)),
                ('judgment_by', models.TextField(blank=True, null=True)),
                ('judgment_status', models.TextField(blank=True, null=True)),
                ('judgment', models.TextField(blank=True, null=True)),
                ('judgment_url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'judgments',
                'managed': False,
            },
        ),
    ]
