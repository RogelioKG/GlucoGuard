# standard library
import random
import string
import time
from typing import Any


def random_form() -> dict[str, Any]:
    """隨機生成表單資訊

    Returns
    -------
    + `volunteer_dict` (dict[str, Any]) : 表單
    """
    volunteer_dict = dict()
    volunteer_dict["formID"] = "233635142103444"
    volunteer_dict["jsExecutionTracker"] = f"..."
    volunteer_dict["submitSource"] = "form"
    volunteer_dict["buildDate"] = str(int(time.time() * 1000)) # unixtime (ms)
    volunteer_dict["HighBP"] = str(random.randint(0, 1))
    volunteer_dict["HighChol"] = str(random.randint(0, 1))
    volunteer_dict["CholCheck"] = str(random.randint(0, 1))
    volunteer_dict["Smoker"] = str(random.randint(0, 1))
    volunteer_dict["Stroke"] = str(random.randint(0, 1))
    volunteer_dict["HeartDiseaseorAttack"] = str(random.randint(0, 1))
    volunteer_dict["PhysActivity"] = str(random.randint(0, 1))
    volunteer_dict["Fruits"] = str(random.randint(0, 1))
    volunteer_dict["Veggies"] = str(random.randint(0, 1))
    volunteer_dict["HvyAlcoholConsump"] = str(random.randint(0, 1))
    volunteer_dict["AnyHealthcare"] = str(random.randint(0, 1))
    volunteer_dict["NoDocbcCost"] = str(random.randint(0, 1))
    volunteer_dict["DiffWalk"] = str(random.randint(0, 1))
    volunteer_dict["Sex"] = str(random.randint(0, 1))
    volunteer_dict["BMI"] = str(truncated_gauss(3, start=15, end=35))
    volunteer_dict["Age"] = str(truncated_gauss(3, start=1, end=13))
    volunteer_dict["Education"] = str(truncated_gauss(1, start=1, end=6))
    volunteer_dict["Income"] = str(truncated_gauss(2, start=1, end=11))
    volunteer_dict["GenHlth"] = str(random.randint(1, 5))
    volunteer_dict["MentHlth"] = str(random.randint(0, 30))
    volunteer_dict["PhysHlth"] = str(random.randint(0, 30))
    volunteer_dict["EmailAddress"] = "".join(random.choice(string.ascii_letters) for _ in range(16)) + "@gmail.com"
    volunteer_dict["formOpenId_V5"] = "..."
    volunteer_dict["timeToSubmit"] = "20"
    volunteer_dict["event_id"] = "..."
    volunteer_dict["validatedNewRequiredFieldIDs"] = '{"new":1}'
    return volunteer_dict


def truncated_gauss(sigma: float, *, start: int, end: int) -> int:
    """回傳隨機整數，其為截斷高斯分布

    Parameters
    ----------
    + `sigma` (float) : 標準差
    + `start` (int) : 下界
    + `end` (int) : 上界 

    Returns
    -------
    + (int) : 隨機整數
    """
    mu = (start + end) / 2
    return int(min(end, max(start, random.gauss(mu, sigma))))

if __name__ == "__main__":
    print(random_form())