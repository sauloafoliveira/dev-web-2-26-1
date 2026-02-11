# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=20)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=52)  # Field name made lowercase.
    continent = models.TextField(db_column='Continent')  # Field name made lowercase. This field type is a guess.
    region = models.CharField(db_column='Region', max_length=26)  # Field name made lowercase.
    #surfacearea = models.DecimalField(db_column='SurfaceArea', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    indepyear = models.SmallIntegerField(db_column='IndepYear', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.
    #lifeexpectancy = models.DecimalField(db_column='LifeExpectancy', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    #gnp = models.DecimalField(db_column='GNP', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    #gnpold = models.DecimalField(db_column='GNPOld', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    localname = models.CharField(db_column='LocalName', max_length=45)  # Field name made lowercase.
    governmentform = models.CharField(db_column='GovernmentForm', max_length=45)  # Field name made lowercase.
    headofstate = models.CharField(db_column='HeadOfState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    capital = models.IntegerField(db_column='Capital', blank=True, null=True)  # Field name made lowercase.
    code2 = models.CharField(db_column='Code2', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return f'{self.name} ({self.code2}): {self.continent} - {self.capital}'


class Countrylanguage(models.Model):
    countrycode = models.OneToOneField(Country, models.DO_NOTHING, db_column='CountryCode', primary_key=True)  # Field name made lowercase. The composite primary key (CountryCode, Language) found, that is not supported. The first column is selected.
    language = models.CharField(db_column='Language', max_length=30)  # Field name made lowercase.
    isofficial = models.TextField(db_column='IsOfficial')  # Field name made lowercase. This field type is a guess.
    percentage = models.DecimalField(db_column='Percentage', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'countrylanguage'
