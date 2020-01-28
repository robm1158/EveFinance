import pandas as pd
import math
import numpy as np
import sqlUpdater
import filterTools


class filterTool:

    def __init__ (self,sql):
        self.sql = sql
