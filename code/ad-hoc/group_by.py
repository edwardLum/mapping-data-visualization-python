import pandas as pd 
import numpy as np


speeds = pd.DataFrame(
    [
        ("bird", "Falconiformes", 389.0),
        ("bird", "Psittaciformes", 24.0),
        ("mammal", "Carnivora", 80.2),
        ("mammal", "Primates", np.nan),
        ("mammal", "Carnivora", 58),
    ],
    index=["falcon", "parrot", "lion", "monkey", "leopard"],
    columns=("class", "order", "max_speed"),
)

class_grouping = speeds.groupby("class")

order_grouping = speeds.groupby("order", axis="columns")

order_grouped = speeds.groupby(["class", "order"])
