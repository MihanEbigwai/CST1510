# completed warm-up

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})

df["percent"] = (df["value"].astype(float) / df["limit"]) * 100
