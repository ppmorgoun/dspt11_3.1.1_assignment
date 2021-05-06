from mymodules import helper_functions as hf
import pandas as pd
import numpy as np

path = '/Users/petr/documents/lambda/units/unit 2/sprint 3/DS-Unit-2-Applied-Modeling/data/project/train.csv'
df = pd.read_csv(path)


hf.train_test_split(df, 0.333)
