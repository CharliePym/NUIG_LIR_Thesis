from django.db import models

# judgments class
class Judgments(models.Model):
    judgment_id = models.BigIntegerField(blank=True, null=False, primary_key=True) # acts as primary key for DB
    neutral_citation = models.TextField(blank=True, null=True)
    judgment_title = models.TextField(blank=True, null=True)
    judgment_date = models.TextField(blank=True, null=True)
    court_name = models.TextField(blank=True, null=True)
    judgment_by = models.TextField(blank=True, null=True)
    judgment_status = models.TextField(blank=True, null=True)
    judgment = models.TextField(blank=True, null=True)
    judgment_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'judgments'

