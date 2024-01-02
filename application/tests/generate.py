# standard library
import random
import time
import string
from typing import Any

def random_form() -> dict[str, Any]:
    """隨機生成表單資訊

    Returns
    -------
    + `volunteer_dict` (dict[str, Any]) : 表單資訊
    """
    volunteer_dict = dict()
    volunteer_dict["formID"] = "233635142103444"
    volunteer_dict["jsExecutionTracker"] = "build-date-1704013390989=>init-started:1704018466372=>validator-called:1704018466378=>validator-mounted-true:1704018466378=>init-complete:1704018466381=>interval-complete:1704018487387=>onsubmit-fired:1704018492697=>submit-validation-passed:1704018492700"
    volunteer_dict["submitSource"] = "form"
    volunteer_dict["buildDate"] = str(int(time.time() * 1000))  # unixtime (ms)
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
    volunteer_dict["BMI"] = str(truncated_gauss(10, start=15, end=65))
    volunteer_dict["Age"] = str(truncated_gauss(3, start=1, end=13))
    volunteer_dict["Education"] = str(truncated_gauss(1, start=1, end=6))
    volunteer_dict["Income"] = str(truncated_gauss(2, start=1, end=11))
    volunteer_dict["GenHlth"] = str(random.randint(1, 5))
    volunteer_dict["MentHlth"] = str(random.randint(0, 30))
    volunteer_dict["PhysHlth"] = str(random.randint(0, 30))
    volunteer_dict["EmailAddress"] = random_var_name(10) + "@gmail.com"
    volunteer_dict["formOpenId_V5"] = "14999403757376451606"
    volunteer_dict["timeToSubmit"] = "20"
    volunteer_dict["event_id"] = "1704018466380_233635142103444_9Ev2l4U"
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
    + -------
    + (int) : 隨機整數
    """
    mu = (start + end) / 2
    return int(min(end, max(start, random.gauss(mu, sigma))))

def random_var_name(n: int) -> str:
    """隨機變數名稱

    Parameters
    ----------
    + `n` (int) : 字串長度 

    Returns
    -------
    + (str) : 隨機變數名稱
    """
    return "".join(random.choice(string.ascii_letters) for _ in range(n))

    # 表單範例
    # ImmutableDict(
    #     [
    #         ("formID", "233635142103444"),
    #         (
    #             "jsExecutionTracker",
    #             "build-date-1704013390989=>init-started:1704018466372=>validator-called:1704018466378=>validator-mounted-true:1704018466378=>init-complete:1704018466381=>interval-complete:1704018487387=>onsubmit-fired:1704018492697=>submit-validation-passed:1704018492700",
    #         ),
    #         ("submitSource", "form"),
    #         ("buildDate", "1704013390989"),
    #         ("HighBP", "1"),
    #         ("HighChol", "1"),
    #         ("CholCheck", "0"),
    #         ("Smoker", "0"),
    #         ("Stroke", "1"),
    #         ("HeartDiseaseorAttack", "0"),
    #         ("PhysActivity", "1"),
    #         ("Fruits", "0"),
    #         ("Veggies", "1"),
    #         ("HvyAlcoholConsump", "0"),
    #         ("AnyHealthcare", "1"),
    #         ("NoDocbcCost", "0"),
    #         ("DiffWalk", "1"),
    #         ("Sex", "0"),
    #         ("BMI", "123"),
    #         ("Age", "11"),
    #         ("Education", "6"),
    #         ("Income", "11"),
    #         ("GenHlth", "3"),
    #         ("MentHlth", "20"),
    #         ("PhysHlth", "12"),
    #         ("EmailAddress", "t126017977@gmail.com"),
    #         ("formOpenId_V5", "14999403757376451606"),
    #         ("timeToSubmit", "20"),
    #         ("event_id", "1704018466380_233635142103444_9Ev2l4U"),
    #         ("validatedNewRequiredFieldIDs", '{"new":1}'),
    #     ]
    # )