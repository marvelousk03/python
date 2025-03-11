15.3

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Generate a random walk
rw = RandomWalk(5000)  # Reduce points from 50,000 to 5,000
rw.fill_walk()

# Set up the plot
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(rw.x_values, rw.y_values, linewidth=1)

# Remove the axes for a cleaner look
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()