import random 
import plotly.express as px
import plotly.figure_factory as ff

dice_result = []
count = []
for i in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum =dice1+dice2
    dice_result.append(sum)
    count.append(i)

#fig = px.bar(x=dice_result, y = count)
#fig.show()


fig = ff.create_distplot([dice_result], ["Addition of two dice values"])
fig.show()