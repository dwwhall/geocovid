from django.db import models

# Create your models here.

class Sequence(models.Model):
    genesequence = models.TextField(primary_key=True, db_column='gene_sequence')
    country = models.TextField(db_column='country')
    stateprovince = models.TextField(db_column='state_province')
    sequencetechnology = models.TextField(db_column='sequence_technology')
    sequencetechnology2 = models.TextField(db_column='sequence_technology2')
    sequencetechnologytype = models.TextField(db_column='sequence_technology_type')

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'sequence'


class Publications(models.Model):
    title = models.TextField(primary_key=True, db_column='title')
    author = models.TextField(db_column='authors')
    abstract = models.TextField(db_column='abstract')
    year = models.IntegerField(db_column='published_year')
    journal = models.TextField(db_column='journal')

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'publications'