import pandas as pd
import numpy as np
d={"days":[1,2,3,4,5,6,7,8,9,10],"steps":[3300,2200,4400,3204,5678,4567,7890,8675,6789,6789,]}
dp=pd.DataFrame(d)
dp["+1000 steps"]=dp["steps"]+1000
fi=dp[dp["+1000 steps"]>7000]["days"]
print("Dataframe:",dp)
print("\n days in which steps were >7000:\n",fi)