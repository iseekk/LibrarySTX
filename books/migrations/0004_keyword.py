# Generated by Django 4.0.1 on 2022-01-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_authors_alter_book_isbn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=255, verbose_name="Wpisz słowa kluczowe oddzielone przecinkiem ','")),
            ],
        ),
    ]
