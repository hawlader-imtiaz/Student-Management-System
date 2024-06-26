# Generated by Django 5.0.1 on 2024-06-25 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_student_age_student_region'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PurchaseBooks',
            new_name='Grade',
        ),
        migrations.RenameModel(
            old_name='Grades',
            new_name='PurchaseBook',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='studentId',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='purchasebook',
            old_name='studentId',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='bookId',
        ),
        migrations.RemoveField(
            model_name='purchasebook',
            name='courseId',
        ),
        migrations.AddField(
            model_name='grade',
            name='course',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='base.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasebook',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.book'),
            preserve_default=False,
        ),
    ]
