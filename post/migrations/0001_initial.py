# Generated by Django 4.1.1 on 2022-10-14 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import post.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bookmarks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True, unique=True)),
                (
                    "category_slug",
                    models.SlugField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True, unique=True)),
                (
                    "sub_category_slug",
                    models.SlugField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="post.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="/images/profile_pics/pngfind.com-placeholder-png-6104451.png",
                        null=True,
                        upload_to="images/profile_pics",
                    ),
                ),
                (
                    "blogger",
                    models.OneToOneField(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500, unique=True)),
                ("slug", models.SlugField(blank=True, max_length=200, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("publish_on", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "image",
                    models.ImageField(
                        default="post/faf75719-9275-4348-b2e1-269eeb2c023b.png",
                        upload_to="post/%d/%m/%y",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Draft"), ("published", "Published")],
                        default="draft",
                        max_length=20,
                    ),
                ),
                ("contents", models.TextField()),
                ("description", models.TextField(blank=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "bookmarks",
                    models.ManyToManyField(
                        blank=True,
                        default=None,
                        related_name="bookmark",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        default=post.models.Category.get_cat,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="post.category",
                    ),
                ),
                (
                    "sub_category",
                    models.ForeignKey(
                        blank=True,
                        default=post.models.SubCategory.get_sub,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="post.subcategory",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "ordering": ("-publish_on",),
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField(max_length=10000, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("publish", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=50)),
                ("status", models.BooleanField(default=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="post.post",
                    ),
                ),
            ],
            options={
                "ordering": ("publish",),
            },
        ),
    ]