# Generated by Django 3.0.11 on 2021-06-08 10:00

from django.db import migrations


def migrate_Photograph_to_MediaObject(apps, schema_editor):
    """
    Populate tree_node fields with systematics values.
    """
    Photograph = apps.get_model("photograph", "Photograph")
    MediaObject = apps.get_model("media_object", "MediaObject")

    # since there is no filterable backwards relation for `profile`
    for photo in Photograph.objects.all():
        # We can not access the profile relation in the migration for whatever
        # reason.
        # So just create MediaObjects from Photographs which are releated via a content_type
        if photo.object_id:
            _file = photo.img.file
            # get the original file name without path remnants
            _file.name = _file.name.split("/")[-1]
            audio_file = None
            if photo.audio:
                audio_file = photo.audio
                audio_file.name = audio_file.name.split("/")[-1]

            MediaObject.objects.create(
                profile_position=photo.profile_position,
                media_format="image",
                file=_file,
                dzi_option=photo.dzi_option,
                img_original_width=photo.img_original_width,
                img_original_height=photo.img_original_height,
                img_original_scale=photo.img_original_scale,
                img_alt=photo.img_alt,
                description=photo.description,
                audio=audio_file,
                date=photo.date,
                author=photo.author,
                license=photo.license,
                content_type=photo.content_type,
                object_id=photo.object_id,
            )


def migrate_MediaObject_to_Photograph(apps, schema_editor):

    Photograph = apps.get_model("photograph", "Photograph")
    Wine = apps.get_model("planty_content", "Wine")

    # we need too loop over all MediaObjects which are images
    # since there is no filterable backwards relation for `profile`
    for profile in Wine.objects.all():
        media_obj = profile.media_objects.all()
        if media_obj.profile:
            _file = media_obj.img.file
            # get the original file name without path remnants
            _file.name = _file.name.split("/")[-1]
            audio_file = None
            if media_obj.audio:
                audio_file = media_obj.audio
                audio_file.name = audio_file.name.split("/")[-1]

            Photograph.objects.create(
                profile_position=media_obj.profile_position,
                media_format="image",
                file=_file,
                img_original_width=media_obj.img_original_width,
                img_original_height=media_obj.img_original_height,
                img_original_scale=media_obj.img_original_scale,
                img_alt=media_obj.img_alt,
                description=media_obj.description,
                audio=audio_file,
                date=media_obj.date,
                author=media_obj.author,
                license=media_obj.license,
            )


class Migration(migrations.Migration):

    dependencies = [
        ("planty_content", "0031_auto_20210604_1954"),
    ]

    operations = [
        migrations.RunPython(
            migrate_Photograph_to_MediaObject, migrate_MediaObject_to_Photograph
        ),
    ]
