# Generated by Django 3.0.11 on 2022-12-09 11:05

import django.db.models.deletion
import mptt.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_treenode_name_attributes'),
        ('planty_plant_content', '0014_auto_20230130_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='tree_node',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='plant_related', related_query_name='plants', to='content.TreeNode'),
        ),
    ]
