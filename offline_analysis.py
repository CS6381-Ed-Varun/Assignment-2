import matplotlib as plt
import pandas as pd
from pathlib import Path

# get the path to the example folder
example_path = Path(__file__).parent

# find all csv with pattern *#*.csv, e.g. adolescent#001.csv
#result_filenames = list(exmaple_pth.glob(
#    'results/2017-12-31_17-46-32/*#*.csv'))

result_filenames = list(example_path.glob('results/result.csv'))

stock_names = [f.stem for f in result_filenames]
df = pd.concat(
        [pd.read_csv(str(f), index_col=0) for f in result_filenames],
        keys=stock_names)
report(df)
