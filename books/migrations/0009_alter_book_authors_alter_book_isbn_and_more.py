# Generated by Django 4.0.1 on 2022-01-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_remove_book_previewlink_book_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.CharField(blank=True, max_length=255, verbose_name='Autorzy'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, max_length=255, verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pageCount',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ilość stron'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishedDate',
            field=models.DateField(blank=True, null=True, verbose_name='Data publikacji'),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.URLField(blank=True, max_length=255, verbose_name='Odnośnik do okładki'),
        ),
    ]
