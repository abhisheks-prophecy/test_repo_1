from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Script_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    import torch
    import math
    dtype = torch.float
    device = torch.device("cpu")
    x = torch.linspace(- math.pi, math.pi, 2000, device = device, dtype = dtype)
    y = torch.sin(x)
    a = torch.randn((), device = device, dtype = dtype)
    print(a)
    out0 = in0

    return out0
