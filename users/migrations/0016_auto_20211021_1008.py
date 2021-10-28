# Generated by Django 3.2.7 on 2021-10-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20211021_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='valid_good_conduct',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=200),
        ),
        migrations.AddField(
            model_name='message',
            name='valid_passport',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='county',
            field=models.CharField(blank=True, choices=[('Marsabit', 'Marsabit'), ('Wajir', 'Wajir'), ('Makueni', 'Makueni'), ('Busia', 'Busia'), ('Laikipia', 'Laikipia'), ('Kisii', 'Kisii'), ('Turkana', 'Turkana'), ('Mombasa', 'Mombasa'), ('Isiolo', 'Isiolo'), ('Meru', 'Meru'), ('Narok', 'Narok'), ('Bungoma', 'Bungoma'), ('Nyandarua', 'Nyandarua'), ('Trans-Nzoia', 'Trans-Nzoia'), ('Taita–Taveta', 'Taita–Taveta'), ('Vihiga', 'Vihiga'), ('Samburu', 'Samburu'), ('Mandera', 'Mandera'), ('Nandi', 'Nandi'), ('Kitui', 'Kitui'), ('Garissa', 'Garissa'), ('Migori', 'Migori'), ('Muranga', 'Muranga'), ('Kajiado', 'Kajiado'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Nakuru', 'Nakuru'), ('Uasin Gishu', 'Uasin Gishu'), ('Kwale', 'Kwale'), ('Nyamira', 'Nyamira'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Tana River', 'Tana River'), ('Nyeri', 'Nyeri'), ('Baringo', 'Baringo'), ('Lamu', 'Lamu'), ('West Pokot', 'West Pokot'), ('Bomet', 'Bomet'), ('Embu', 'Embu'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Siaya', 'Siaya'), ('Kirinyaga', 'Kirinyaga'), ('Machakos', 'Machakos'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Kakamega', 'Kakamega'), ('Kericho', 'Kericho'), ('Nairobi', 'Nairobi')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='education_level',
            field=models.CharField(blank=True, choices=[('High School', 'High School'), ('Primary School', 'Primary School'), ('University', 'University'), ('College', 'College')], max_length=200, null=True),
        ),
    ]
