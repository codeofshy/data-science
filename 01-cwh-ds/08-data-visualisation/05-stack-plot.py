# excercise : displaying my schedule in stackplot
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]
coding = [7,6,4,5,6,7,4]
exploratory_data_analysis = [6,6,8,7,9,7,11]
netflix = [1,2,1,4,1,2,3]
content_creation = [0,0,0,1,0,0,0.5]

labels = ["Coding", "coding", "exploratory_data_analysis", "Content creation"]
colors = ['skyblue', 'lightgreen', 'gold', 'lightcoral']

plt.figure(figsize=(10,6))    # charts scale size in inches
plt.stackplot(
    days, 
    coding, 
    exploratory_data_analysis, 
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