# standard library
import random


def truncated_gauss(start: int, end: int, *, sigma: float) -> int:
    """回傳隨機整數，其為截斷高斯分布

    Parameters
    ----------
    + `start` (int) : 下界
    + `end` (int) : 上界
    + `sigma` (float) : 標準差 

    Returns
    -------
    + (int) : 隨機整數
    """
    mu = (start + end) / 2
    return int(min(end, max(start, random.gauss(mu, sigma))))
