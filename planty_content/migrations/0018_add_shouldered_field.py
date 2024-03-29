# Generated by Django 3.0.11 on 2021-03-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planty_content", "0017_auto_20210329_1427"),
    ]

    operations = [
        migrations.AddField(
            model_name="grape",
            name="shouldered",
            field=models.CharField(
                choices=[("ja", "ja"), ("nein", "nein"), ("teilweise", "teilweise")],
                default="ja",
                max_length=9,
                verbose_name="Geschultert",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="grape",
            name="density",
            field=models.CharField(
                choices=[
                    ("lockerbeerig", "lockerbeerig"),
                    ("mitteldicht", "mitteldicht"),
                    ("kompakt", "kompakt"),
                ],
                max_length=12,
                verbose_name="Dichte",
            ),
        ),
        migrations.AlterField(
            model_name="grape",
            name="form",
            field=models.CharField(
                choices=[
                    ("zylindrisch", "zylindrisch"),
                    ("konisch", "konisch"),
                    ("kegelförmig", "kegelförmig"),
                    ("walzenförmig", "walzenförmig"),
                ],
                max_length=24,
                verbose_name="Form",
            ),
        ),
    ]
