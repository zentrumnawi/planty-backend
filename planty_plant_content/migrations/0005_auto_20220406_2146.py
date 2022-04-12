# Generated by Django 3.0.11 on 2022-04-06 19:46

from django.db import migrations, models
import django.db.models.deletion
import planty_plant_content.models


class Migration(migrations.Migration):

    dependencies = [
        ('planty_plant_content', '0004_auto_20220406_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blossom',
            name='extras',
            field=models.TextField(blank=True, help_text='', max_length=500, null=True, verbose_name='Weitere Merkmale '),
        ),
        migrations.AlterField(
            model_name='blossom',
            name='note_to_bloom',
            field=models.TextField(blank=True, help_text='', max_length=500, null=True, verbose_name='Hinweise zur Blütezeit'),
        ),
        migrations.CreateModel(
            name='PlantationAndCare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantation_time', models.CharField(blank=True, max_length=100, null=True, verbose_name='Empfohlener Pflanzzeitpunkt ')),
                ('eruption', models.CharField(blank=True, choices=[('ja', 'ja'), ('nein', 'nein')], max_length=4, null=True, verbose_name='Stockausschlagsfähigkeit')),
                ('cutting', models.TextField(blank=True, help_text='Verträglichkeit, Zeitpunkt', max_length=500, null=True, verbose_name='Schnitt')),
                ('preservation', models.TextField(blank=True, max_length=500, null=True, verbose_name='Verjüngung/Erhaltung ')),
                ('fertilization', models.TextField(blank=True, help_text='in Verwendung', max_length=500, null=True, verbose_name='Düngung/Wachstumsförderung ')),
                ('soil_treatment', models.TextField(blank=True, max_length=500, null=True, verbose_name='Bodenbearbeitung')),
                ('hibernation', planty_plant_content.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[('1', 'frostfrei'), ('2', 'kühl'), ('3', 'warm'), ('4', 'Kalthaus'), ('5', 'Warmhaus'), ('6', 'hell'), ('7', 'dunkel'), ('8', 'Freiland'), ('9', 'Winterschutz'), ('10', 'beheizterWinterschutz'), ('11', 'Nässeschutz')], max_length=2), blank=True, null=True, size=None, verbose_name='Überwinterung')),
                ('extra', models.TextField(blank=True, max_length=500, null=True, verbose_name='Weiteres zur Pflanzung und Pflege')),
                ('plant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plantation_and_creation', to='planty_plant_content.Plant', verbose_name='Pflanze')),
            ],
            options={
                'verbose_name': 'Pflanzung und Pflege',
                'verbose_name_plural': 'Pflanzungen und Pflege',
            },
        ),
    ]