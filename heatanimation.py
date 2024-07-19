import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('/Users/archismanbasu/Documents/heattt/matrix_data.csv')

# Clean the data by replacing non-numeric characters with NaN and dropping NaN values
df = df.apply(pd.to_numeric, errors='coerce').dropna()

# Convert the DataFrame to a 2D numpy array for easier manipulation
data = df.to_numpy()

# Determine the grid size for the heatmap
num_columns = data.shape[1]
grid_size = int(math.ceil(math.sqrt(num_columns)))

# Pad the data with NaNs if necessary to fit the grid
padded_data = np.pad(data, ((0, 0), (0, grid_size ** 2 - num_columns)), mode='constant', constant_values=np.nan)

# Reshape the data for each time step into a 2D array
frames = padded_data.reshape(-1, grid_size, grid_size)

# Set up the plot with adjusted figure size
fig, ax = plt.subplots(figsize=(10, 10))
cbar_ax = fig.add_axes([0.92, 0.3, 0.02, 0.4])  # Position the color bar

# Function to update the heatmap for each frame
def update(frame):
    ax.clear()
    sns.heatmap(frame, cmap='viridis', cbar=True, ax=ax, cbar_ax=cbar_ax, vmin=data.min(), vmax=data.max(), annot=False, square=True)
    ax.set_title('Heat Map of Arduino Output')
    ax.set_xlabel('X Axis Label')  # Replace with your actual x-axis label
    ax.set_ylabel('Y Axis Label')  # Replace with your actual y-axis label

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, repeat=False)

# Save the animation as a GIF file
ani.save('/Users/archismanbasu/Documents/heattt/heatmap_animation.gif', writer='pillow', fps=10)

plt.show()
