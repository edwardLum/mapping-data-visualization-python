import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

d = {"b": 1, "a": 0, "c": 2}

pd.Series(d, index=["b", "c", "d", "a"])
