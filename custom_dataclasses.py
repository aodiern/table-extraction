from dataclasses import dataclass
from typing import List
import pandas as pd
import numpy as np

# класс извлеченной таблицы
@dataclass
class ExtractedTable:
    source: str
    dataframe: pd.DataFrame

# класс результата извлечения
@dataclass
class ExtractionResult:
    method: str
    tables: List[ExtractedTable]
    debug_images: List[np.ndarray]
