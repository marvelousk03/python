# import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)

# ax.plot(input_values,squares, linewidth=3)
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# ax.tick_params(labelsize=14)

# plt.show()



# import matplotlib.pyplot as plt

# # Group members and their values (each one is 1 lower than the previous)
# members = ["Ethan", "Marvelous", "Pierre", "Ronny"]
# values = [70, 69, 68, 67]  # Descending order for cool effect

# # Create an even cooler line graph
# plt.figure(figsize=(10, 6))
# plt.plot(members, values, marker="o", linestyle="-", color="#FF4500", linewidth=4, 
#          markersize=12, markerfacecolor="black", markeredgewidth=2, markeredgecolor="yellow")

# # Add title and labels with more dramatic styling
# plt.title("⚡ 404 Avengers - Power Levels ⚡", fontsize=20, fontweight="bold", color="purple")
# plt.xlabel("Members", fontsize=14, fontweight="bold", color="darkred")
# plt.ylabel("Score", fontsize=14, fontweight="bold", color="darkblue")

# # Add value labels with cooler styling
# for i, v in enumerate(values):
#     plt.text(i, v + 1, str(v), ha="center", fontsize=14, fontweight="bold", color="white",
#              bbox=dict(facecolor="blue", edgecolor="white", boxstyle="round,pad=0.5"))

# # Enhanced grid with neon-style glow
# plt.grid(axis="y", linestyle="--", alpha=0.3, color="cyan")

# # Dark background for a futuristic feel
# plt.gca().set_facecolor("#222222")

# # Show the graph
# plt.show()


# import matplotlib.pyplot as plt

# # Group members and their contributions
# members = ["Ethan", "Marvelous", "Pierre", "Ronny"]
# contributions = [48, 46, 27, 22]  

# # Create a visually appealing line graph
# plt.figure(figsize=(9, 5))
# plt.plot(members, contributions, marker="o", linestyle="-", color="#FF4500", linewidth=4, 
#          markersize=12, markerfacecolor="black", markeredgewidth=2, markeredgecolor="yellow")

# # Add title and labels with dramatic styling
# plt.title(" 404 Avengers - GitHub Contributions ", fontsize=20, fontweight="bold", color="purple")
# plt.xlabel("Members", fontsize=14, fontweight="bold", color="darkred")
# plt.ylabel("Number of Contributions", fontsize=14, fontweight="bold", color="darkblue")

# # Add value labels with enhanced styling
# for i, v in enumerate(contributions):
#     plt.text(i, v + 1, str(v), ha="center", fontsize=14, fontweight="bold", color="white",
#              bbox=dict(facecolor="blue", edgecolor="white", boxstyle="round,pad=0.5"))

# # Enhanced grid with neon-style glow
# plt.grid(axis="y", linestyle="--",  color="cyan")

# # Dark background for a futuristic feel
# plt.gca().set_facecolor("#222222")

# # Show the graph
# plt.show()


from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)