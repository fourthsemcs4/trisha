from matplotlib import pyplot as p
import numpy as n
x=n.random.normal(180,5,200)
p.hist(x,color='red')
p.xlabel("height in cm"),p.ylabel("people")
p.title("height of 200 people")
>>>>>>> f38c4406717eb7ed4f6577e26d3c2ffe1b3c851d
p.show()
