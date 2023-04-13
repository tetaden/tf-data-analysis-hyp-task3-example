import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 415542660 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alternative = "greater"
    ans = mannwhitneyu(x, y, alternative=alternative).pvalue < 0.03
    return ans # Ваш ответ, True или False
