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


# from random import choice

# class RandomWalk:
#     """A class to generate random walks."""

#     def __init__(self, num_points=5000):
#         self.num_points = num_points
#         self.x_values = [0]
#         self.y_values = [0]

#     def get_step(self):
#         """Determine the direction and distance for a step."""
#         direction = choice([1, -1])
#         distance = choice([0, 1, 2, 3, 4])
#         return direction * distance

#     def fill_walk(self):
#         """Calculate all the points in the walk."""
#         while len(self.x_values) < self.num_points:
#             x_step = self.get_step()
#             y_step = self.get_step()

#             if x_step == 0 and y_step == 0:
#                 continue

#             self.x_values.append(self.x_values[-1] + x_step)
#             self.y_values.append(self.y_values[-1] + y_step)


# import numpy as np
# import plotly.express as px

# # Simulating 1000 gaming matches
# np.random.seed(42)
# matches = 1000  
# snacks_per_match = np.random.randint(0, 10, size=matches)  # Random snacks eaten per match (0-9)

# # Create interactive cyberpunk histogram
# fig = px.histogram(
#     x=snacks_per_match, 
#     nbins=10, 
#     title="🍕 Gamer Snack Consumption Per Match 🎮 (Neon Edition)",
#     labels={"x": "Number of Snacks Devoured", "y": "Frequency"},
#     color_discrete_sequence=["#00FFAA"]
# )

# # Cyberpunk styling
# fig.update_layout(
#     template="plotly_dark",
#     plot_bgcolor="#1C1C1C",  # Dark background
#     paper_bgcolor="#121212",  # Outer frame background
#     font=dict(color="#00FFFF", size=16),
#     xaxis=dict(
#         title_font=dict(size=20, color="lightblue"),
#         tickfont=dict(color="cyan"),
#         gridcolor="magenta"
#     ),
#     yaxis=dict(
#         title_font=dict(size=20, color="lightblue"),
#         tickfont=dict(color="cyan"),
#         gridcolor="magenta"
#     )
# )

# # Save as HTML and open in the browser (Optional)
# fig.write_html("gamer_snacks.html", auto_open=True)

# # Show in Jupyter Notebook (if running in one)
# fig.show()


# import numpy as np
# import plotly.express as px

# # Simulate snack consumption in 1000 gaming matches
# np.random.seed(42)
# matches = 1000  
# snacks_per_match = np.random.randint(0, 10, size=matches)  # Random snacks eaten per match (0-9)

# # Create an interactive histogram
# fig = px.histogram(
#     x=snacks_per_match, 
#     nbins=10, 
#     title="🎮 Gamer Snack Consumption Per Match 🍕",
#     labels={"x": "Number of Snacks", "y": "Frequency"},
#     color_discrete_sequence=["#00FFAA"]  # Neon green
# )

# # Customize the look (Cyberpunk theme)
# fig.update_layout(
#     template="plotly_dark",
#     plot_bgcolor="#1C1C1C",  # Dark background
#     paper_bgcolor="#121212",  # Outer frame background
#     font=dict(color="cyan", size=16),
#     xaxis=dict(
#         title_font=dict(size=18, color="lightblue"),
#         tickfont=dict(color="cyan")
#     ),
#     yaxis=dict(
#         title_font=dict(size=18, color="lightblue"),
#         tickfont=dict(color="cyan")
#     )
# )

# # Save as HTML and open in the browser
# fig.write_html("gamer_snacks.html", auto_open=True)

# # Show in Jupyter Notebook (if running there)
# fig.show()

import numpy as np
import plotly.graph_objects as go

# Simulating 1000 rounds of a card game
np.random.seed(42)
rounds = 1000  # Number of rounds played
wins_per_round = np.random.randint(0, 10, size=rounds)  # Wins per round (0-9)

# Set up Plotly histogram with interactive animation
fig = go.Figure()

# Add a histogram trace with animation and hover effects
fig.add_trace(go.Histogram(
    x=wins_per_round,
    nbinsx=10,  # Only include this once
    marker=dict(
        color='cyan',  # Neon color for bars
        line=dict(color='magenta', width=3),  # Neon outline for bars
        opacity=0.9,
        colorbar=dict(title="Neon Glow")  # Add colorbar for effect
    ),
    name="Wins per Round",
    hoverinfo="x+y",  # Display hover info
    orientation="v"
))

# Customize layout for a futuristic look
fig.update_layout(
    title="🌟 Ultra-Cool Cyberpunk Wins in Card Game 🃏",
    title_font=dict(family="Arial", size=30, color="cyan"),
    xaxis=dict(
        title="Number of Wins per Round",
        title_font=dict(family="Arial", size=20, color="lightblue"),
        tickfont=dict(color="cyan"),
        showgrid=True,
        gridcolor="white",
        zeroline=False
    ),
    yaxis=dict(
        title="Frequency",
        title_font=dict(family="Arial", size=20, color="lightblue"),
        tickfont=dict(color="cyan"),
        showgrid=True,
        gridcolor="white",
        zeroline=False
    ),
    plot_bgcolor="#121212",  # Dark background for the plot
    paper_bgcolor="#080808",  # Dark background for the page
    showlegend=False,
    margin=dict(l=40, r=40, t=80, b=40),  # Adjust margins for better spacing
    font=dict(family="Arial, sans-serif", color="white", size=16),
    updatemenus=[  # Adding play and pause buttons for animation
        dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)])]
        )
    ],
)

# Add a glowing shadow effect to bars (for 3D-like depth)
fig.update_traces(marker=dict(
    line=dict(color='white', width=1),  # Outline for shadow effect
))

# Show the plot
fig.show()