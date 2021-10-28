# Generated by Django 3.2.7 on 2021-10-21 11:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20211021_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='county',
            field=models.CharField(blank=True, choices=[('Turkana', 'Turkana'), ('Nyandarua', 'Nyandarua'), ('Lamu', 'Lamu'), ('Kwale', 'Kwale'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Bungoma', 'Bungoma'), ('Meru', 'Meru'), ('Kitui', 'Kitui'), ('Tana River', 'Tana River'), ('Machakos', 'Machakos'), ('Mandera', 'Mandera'), ('Migori', 'Migori'), ('Kakamega', 'Kakamega'), ('Nakuru', 'Nakuru'), ('Kirinyaga', 'Kirinyaga'), ('Uasin Gishu', 'Uasin Gishu'), ('Busia', 'Busia'), ('West Pokot', 'West Pokot'), ('Nyeri', 'Nyeri'), ('Baringo', 'Baringo'), ('Kericho', 'Kericho'), ('Garissa', 'Garissa'), ('Embu', 'Embu'), ('Trans-Nzoia', 'Trans-Nzoia'), ('Homa Bay', 'Homa Bay'), ('Kisii', 'Kisii'), ('Kilifi', 'Kilifi'), ('Nairobi', 'Nairobi'), ('Kiambu', 'Kiambu'), ('Kajiado', 'Kajiado'), ('Kisumu', 'Kisumu'), ('Laikipia', 'Laikipia'), ('Makueni', 'Makueni'), ('Samburu', 'Samburu'), ('Nyamira', 'Nyamira'), ('Narok', 'Narok'), ('Nandi', 'Nandi'), ('Muranga', 'Muranga'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Siaya', 'Siaya'), ('Wajir', 'Wajir'), ('Mombasa', 'Mombasa'), ('Marsabit', 'Marsabit'), ('Vihiga', 'Vihiga'), ('Bomet', 'Bomet'), ('Taita–Taveta', 'Taita–Taveta'), ('Isiolo', 'Isiolo')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='education_level',
            field=models.CharField(blank=True, choices=[('University', 'University'), ('College', 'College'), ('High School', 'High School'), ('Primary School', 'Primary School')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('education_level', models.CharField(blank=True, choices=[('University', 'University'), ('College', 'College'), ('High School', 'High School'), ('Primary School', 'Primary School')], max_length=200, null=True)),
                ('valid_passport', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=200)),
                ('valid_good_conduct', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=200)),
                ('county', models.CharField(blank=True, choices=[('Turkana', 'Turkana'), ('Nyandarua', 'Nyandarua'), ('Lamu', 'Lamu'), ('Kwale', 'Kwale'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Bungoma', 'Bungoma'), ('Meru', 'Meru'), ('Kitui', 'Kitui'), ('Tana River', 'Tana River'), ('Machakos', 'Machakos'), ('Mandera', 'Mandera'), ('Migori', 'Migori'), ('Kakamega', 'Kakamega'), ('Nakuru', 'Nakuru'), ('Kirinyaga', 'Kirinyaga'), ('Uasin Gishu', 'Uasin Gishu'), ('Busia', 'Busia'), ('West Pokot', 'West Pokot'), ('Nyeri', 'Nyeri'), ('Baringo', 'Baringo'), ('Kericho', 'Kericho'), ('Garissa', 'Garissa'), ('Embu', 'Embu'), ('Trans-Nzoia', 'Trans-Nzoia'), ('Homa Bay', 'Homa Bay'), ('Kisii', 'Kisii'), ('Kilifi', 'Kilifi'), ('Nairobi', 'Nairobi'), ('Kiambu', 'Kiambu'), ('Kajiado', 'Kajiado'), ('Kisumu', 'Kisumu'), ('Laikipia', 'Laikipia'), ('Makueni', 'Makueni'), ('Samburu', 'Samburu'), ('Nyamira', 'Nyamira'), ('Narok', 'Narok'), ('Nandi', 'Nandi'), ('Muranga', 'Muranga'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Siaya', 'Siaya'), ('Wajir', 'Wajir'), ('Mombasa', 'Mombasa'), ('Marsabit', 'Marsabit'), ('Vihiga', 'Vihiga'), ('Bomet', 'Bomet'), ('Taita–Taveta', 'Taita–Taveta'), ('Isiolo', 'Isiolo')], max_length=200, null=True)),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='application', to='users.profile')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
    ]
