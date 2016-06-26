import os
import sys

sys.path.append(os.path.split(os.path.realpath(__file__))[0])

import Stock_ETL.backend_jobs as bj

if __name__ == '__main__':
    bj.daily_run()