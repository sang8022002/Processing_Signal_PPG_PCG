import matplotlib.pyplot as plt

# Read data from the file
with open('mean_data.txt', 'r') as file:
    data = file.readlines()

# Extract x and y values from the data
x = []
y = []
for line in data:
    values = line.strip().split(',')
    x.append(float(values[0]))
    # y.append(float(values[1]))

# Plot the graph
plt.plot(x)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Mean Data')
plt.show()