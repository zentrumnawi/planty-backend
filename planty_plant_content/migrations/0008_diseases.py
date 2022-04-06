# Generated by Django 3.0.11 on 2022-04-06 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planty_plant_content', '0007_faunausability_humanusability_toxicity_usability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseases', models.CharField(blank=True, max_length=100, null=True, verbose_name='Krankheiten/Schädlinge')),
                ('physiology_damage', models.CharField(blank=True, max_length=100, null=True, verbose_name='Physiologische Schäden')),
                ('resistances', models.TextField(blank=True, max_length=500, null=True, verbose_name='Resistenzen/ Immunitäten/ Geringe Anfälligkeiten')),
                ('culture_protection', models.TextField(blank=True, max_length=500, null=True, verbose_name='Kulturschutzmaßnahmen')),
                ('biological_protection', models.TextField(blank=True, max_length=500, null=True, verbose_name='Biologische Kulturschutzmaßnahmen')),
                ('plant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='disease', to='planty_plant_content.Plant', verbose_name='Pflanze')),
            ],
            options={
                'verbose_name': 'Krankheiten / Schädlinge / Resistenzen',
                'verbose_name_plural': 'Krankheiten / Schädlinge / Resistenzen',
            },
        ),
    ]
