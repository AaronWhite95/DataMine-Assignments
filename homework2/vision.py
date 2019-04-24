import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json

with open("./results/freq_set.json") as f1:
    freq = [json.loads(each) for each in f1.readlines()]

with open("./results/rules.json") as f2:
    rules = [json.loads(each) for each in f2.readlines()]

freq_sup = [each["sup"] for each in freq]
plt.boxplot(freq_sup)
plt.ylabel("Frequent item")
plt.show()

rules_sup = [each["sup"] for each in rules]
rules_conf = [each["conf"] for each in rules]
rules_lift = [each["lift"] for each in rules]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(rules_sup, rules_conf, rules_lift)

ax.set_zlabel('Lift', fontdict={'size': 15})
ax.set_ylabel('Conf', fontdict={'size': 15})
ax.set_xlabel('Sup', fontdict={'size': 15})
plt.show()
