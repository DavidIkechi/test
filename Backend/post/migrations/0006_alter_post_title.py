# Generated by Django 4.1.1 on 2022-09-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0005_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
