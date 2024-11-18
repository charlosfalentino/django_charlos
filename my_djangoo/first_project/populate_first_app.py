import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Fake population script
import random
from first_app.models import Topic, Webpage, AccesRecord
from faker import Faker

fakegen = Faker()
topics = ["Social", "Search", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        topic = add_topic()  # Ambil topik
        fake_url = fakegen.url()  # Data palsu untuk URL
        fake_date = fakegen.date()  # Data palsu untuk tanggal
        fake_name = fakegen.company()  # Data palsu untuk nama perusahaan
        # Perbaikan: gunakan topic, bukan top
        webpg = Webpage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]
        acc_record = AccesRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script.....")
    populate(20)
    print("Populating Complete")
