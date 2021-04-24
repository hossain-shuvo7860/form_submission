# Generated by Django 3.0.3 on 2021-04-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardians', '0002_guardianinfo_student_reg_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardianinfo',
            name='applicant_gender',
            field=models.PositiveIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Both')], null=True, verbose_name='Applicant Gender'),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='marital_status',
            field=models.PositiveIntegerField(choices=[(1, 'Married'), (2, 'Unmarried'), (3, 'Divorced'), (4, 'Widow'), (5, 'Widower')], null=True, verbose_name='Applicant Marital Status'),
        ),
    ]
