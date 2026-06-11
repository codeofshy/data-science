# excercise : displaying my schedule in stackplot
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]
coding = [5,6,3,3,6,7,8]
sleeping = [8,8,9,10,9,10,11]
netflix = [4,2,3,4,1,2,2]
content_creation = [0,0,0,2,0,0,0.5]

labels = ["Coding", "Sleeping", "Netflix", "Content creation"]
colors = ['skyblue', 'lightgreen', 'gold', 'lightcoral']

plt.figure(figsize=(10,6))    # charts scale size in inches
plt.stackplot(
    days, 
    coding, 
    sleeping, 
    netflix, 
    content_creation, 
    labels=labels, 
    colors=colors, 
    alpha=0.8
)

plt.xlabel('Days')
plt.ylabel('Hours')
plt.legend(loc='best')
plt.title("Shayan's schedule")
plt.grid(True)
plt.show()