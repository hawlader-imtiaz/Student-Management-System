# Generated by Django 5.0.1 on 2024-06-25 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.course')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseBooks',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.book')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
