# Generated by Django 3.2.16 on 2023-07-13 14:15

from django.db import migrations, models

def move_bot_name_to_name(apps, schema_editor):
    Plant = apps.get_model("planty_plant_content", "Plant")
    for obj in Plant.objects.all():
        obj.general_information.name = obj.taxonomy.bot_name
        obj.general_information.save()


def move_name_to_bot_name(apps, schema_editor):
    Plant = apps.get_model("planty_plant_content", "Plant")
    for obj in Plant.objects.all():
        obj.taxonomy.bot_name = obj.general_information.name
        obj.taxonomy.save()


class Migration(migrations.Migration):

    dependencies = [
        ('planty_plant_content', '0024_generalinformation_sub_name'),
    ]

    operations = [
        migrations.RunPython(move_bot_name_to_name, move_name_to_bot_name),
        migrations.RemoveField(
            model_name='taxonomy',
            name='bot_name',
        ),
        migrations.AlterField(
            model_name='generalinformation',
            name='name',
            field=models.CharField(help_text='Gattung und Art, ggf. Unterart/ Variation, ggf. Sorte', max_length=100, verbose_name='Botanischer Name'),
        ),
    ]
