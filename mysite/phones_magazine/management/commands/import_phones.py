from django.core.management.base import BaseCommand
from ...models import Phone
import csv
from datetime import datetime
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Import phones from CSV'

    def handle(self, *args, **options):
        csv_path = os.path.join(settings.BASE_DIR, 'data', 'phones.csv')

        with open(csv_path, 'r', encoding='utf-8-sig') as file:
            lines = [line.strip().strip('"') for line in file.readlines() if line.strip()]

            header = lines[0].split(';')
            print("Заголовки:", header)

            # Обрабатываем данные
            for line in lines[1:]:
                values = line.split(';')
                if len(values) != len(header):
                    continue

                row = dict(zip(header, values))
                print("Обрабатываемая строка:", row)

                Phone.objects.create(
                    id=int(row['id']),
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=datetime.strptime(row['release_date'], '%Y-%m-%d').date(),
                    lte_exists=row['lte_exists'].lower() == 'true',
                )

        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы!'))