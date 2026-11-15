# Парсер PEP на Scrapy

Учебный проект на Python. Паук Scrapy открывает числовой индекс PEP (Python Enhancement Proposals), переходит по ссылкам на документы и извлекает из каждой страницы номер, название и статус. Scrapy сохраняет записи в CSV, а пайплайн подсчитывает количество документов по статусам.

## Запуск в Linux или WSL

Проверено на Python 3.12. Для обхода каталога нужен интернет.

```bash
git clone https://github.com/anastasia-D/pep-scrapy-parser.git
cd pep-scrapy-parser
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
scrapy crawl pep
```

## Результаты

После обхода файлы появятся в папке `results/`.

| Файл | Содержимое |
| --- | --- |
| `pep_<дата-время>.csv` | Номер, название и статус каждого успешно прочитанного PEP |
| `status_summary_<дата-время>.csv` | Количество PEP в каждом статусе и итоговая строка `Total` |

Ошибки загрузки и страницы с отсутствующими полями видны в журнале Scrapy.
