import logging
import requests
from rq.exceptions import RequestException


logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

success_logger = logging.getLogger('success')
success_logger.setLevel(logging.INFO)
success_handler = logging.FileHandler('success_responses.log')
success_handler.setLevel(logging.INFO)
success_logger.addHandler(success_handler)

bad_logger = logging.getLogger('bad')
bad_logger.setLevel(logging.WARNING)
bad_handler = logging.FileHandler('bad_responses.log')
bad_handler.setLevel(logging.WARNING)
bad_logger.addHandler(bad_handler)

blocked_logger = logging.getLogger('blocked')
blocked_logger.setLevel(logging.ERROR)
blocked_handler = logging.FileHandler('blocked_responses.log')
blocked_handler.setLevel(logging.ERROR)
blocked_logger.addHandler(blocked_handler)


sites = [
    'https://www.youtube.com/',
    'https://wikipedia.org',
    'https://yahoo.com',
    'https://yandex.ru',
    'https://whatsapp.com',
    'https://amazon.com',
    'https://www.ozon.ru',
    'https://instagram.com',
    'https://twitter.com'
]

for site in sites:
    try:
        response = requests.get(site)
        if response.status_code == 200:
            success_logger.info(f"'{site}', response - 200")
        else:
            bad_logger.warning(f"'{site}', response - {response.status_code}")
    except RequestException:
        blocked_logger.error(f"ERROR: {site}, NO CONNECTION")