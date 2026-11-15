import csv

from collections import Counter
from datetime import UTC, datetime
from pathlib import Path


class PepParsePipeline:
    def open_spider(self):
        self.status_counts = Counter()

    def process_item(self, item):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self):
        if not self.status_counts:
            return

        results_dir = Path('results')
        results_dir.mkdir(exist_ok=True)
        timestamp = datetime.now(UTC).strftime('%Y-%m-%dT%H-%M-%S.%f')
        summary = results_dir / f'status_summary_{timestamp}.csv'
        total = sum(self.status_counts.values())
        with summary.open('w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(sorted(self.status_counts.items()))
            writer.writerow(['Total', total])
