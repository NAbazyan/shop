from django.core.management.base import BaseCommand
from apps.market.models import Market
from unidecode import unidecode

BATCH_SIZE = 1000

class Command(BaseCommand):
    help = 'Create slugs for all markets (optimized)'

    def handle(self, *args, **kwargs):
        count = 0
        batch = []

        for market in Market.objects.iterator():            
            transliterated_name = unidecode(market.name)
            market.slug = transliterated_name.lower().replace(' ', '-')
            batch.append(market)
            count += 1

            if len(batch) >= BATCH_SIZE:
                self.bulk_update_markets(batch)
                self.stdout.write(f'Updated {count} records...')
                batch = []

        if batch:
            self.bulk_update_markets(batch)
            self.stdout.write(f'Updated {count} records (final batch).')

        self.stdout.write(self.style.SUCCESS('✅ Slugs successfully created for all markets.'))

    def bulk_update_markets(self, markets):
        Market.objects.bulk_update(markets, ['slug'])
