# Generated by Django 4.1.1 on 2022-09-20 14:38

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("post", "0002_rename_category_category_name_rename_tags_tag_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="tags",
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
