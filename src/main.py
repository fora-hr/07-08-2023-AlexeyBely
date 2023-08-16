import logging

import fora
from core.config import settings


logger = logging.getLogger(__name__)
        

def main():
    with open(settings.competitors2_path, 'r') as f:           
        competitors2 = f.read()
        f.close()
    competition = fora.ForaResults(competitors2)
    with open(settings.results_path, 'r', encoding='utf-8-sig') as f:           
        results = f.read()
        f.close()
    formated_results = competition.format_results(results)
    logger.info(f'{formated_results}')


if __name__ == '__main__':
    main()
