import logging
import json
from datetime import datetime

from . import messages 

logging.getLogger('backoff').addHandler(logging.StreamHandler())


class ForaResults:
    """Formation of results of sports tests."""

    def __init__(self, competitors2: dict):
        try:
            self.competitors = json.loads(competitors2)
        except json.decoder.JSONDecodeError:
            print('Fault json in file competitors2 !!!')
            raise

    def format_results(self, results_run: str) -> list:
        """List formatting results."""
        sorted_results = sorted(self._calc_results_run(results_run),
                                key=lambda result: result[1])
        formated_results_run = []
        place_honor = 1
        for bib_num, delta_time in sorted_results:
            competitor = self.competitors[bib_num]
            formated_results_run.append(
                (
                    place_honor,
                    bib_num,
                    competitor['Name'],
                    competitor['Surname'],
                    str(delta_time),
                )
            )
            place_honor += 1
        return formated_results_run

    def _calc_results_run(self, results_run: str) -> list:
        """Calculate and check data results."""
        bib_numbers_and_times = []
        result_run_list = results_run.splitlines()
        for index_line in range(int(len(result_run_list) / 2) - 2):
            num_line = index_line * 2
            run_start = result_run_list[num_line].split()
            run_finish = result_run_list[num_line + 1].split()
            if run_start[0] != run_finish[0]:
                raise ValueError(messages.ERROR_BIB_NUMBER, str(num_line * 2),
                                 result_run_list[num_line])
            if (run_start[1] != 'start') | (run_finish[1] != 'finish'):
                raise ValueError(messages.ERROR_TAG_START_FINISH, str(num_line * 2),
                                 result_run_list[num_line])    
            time_result = (datetime.strptime(run_finish[2], '%H:%M:%S,%f')
                           - datetime.strptime(run_start[2], '%H:%M:%S,%f'))
            bib_numbers_and_times.append((run_start[0], time_result))
        return bib_numbers_and_times
