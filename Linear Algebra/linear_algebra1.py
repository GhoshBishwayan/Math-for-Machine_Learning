# Import NumPy library for numerical operations
# We use it here to create an array of time values
import numpy as np

# Import Matplotlib's pyplot module for plotting graphs
import matplotlib.pyplot as plt


# -----------------------------
# PROBLEM CONTEXT
# Cop chasing the robber
# -----------------------------


# Create an array of time values
# np.linspace(start, end, number_of_points)
# This creates 1000 evenly spaced values between 0 and 40 minutes
t = np.linspace(0, 40, 1000)


# -----------------------------
# DISTANCE EQUATIONS
# -----------------------------
rob_spd_in_hr = int(input("Robbers car speed?: "))
cop_spd_in_hr = int(input("Cops car speed?: "))
cop_start_delay = int(input("How late does cop start his car?: "))

# Distance travelled by the robber
# Formula: d = speed × time
# Robber speed = 2.5 km per minute
# So: d_r(t) = 2.5t
d_r = (rob_spd_in_hr/60) * t


# Distance travelled by the cop
# Cop starts 5 minutes late, so (t - 5)
# Cop speed = 3 km per minute
# So: d_c(t) = 3(t - 5)
d_c = (cop_spd_in_hr/60) * (t - cop_start_delay)

# Solve interception time algebraically
t_intercept = (cop_spd_in_hr/60) * cop_start_delay / ((cop_spd_in_hr/60) - (rob_spd_in_hr/60))   # derived from equations

# Distance at interception (use robber or cop formula)
d_intercept = (rob_spd_in_hr/60) * t_intercept

# -----------------------------
# PLOTTING SETUP
# -----------------------------


# Create a figure and axes object
# fig → whole canvas
# ax  → plotting area (recommended professional style)
fig, ax = plt.subplots()


# Set the title of the graph
plt.title('A Bank Robber Chase Prediction')


# Label the x-axis
plt.xlabel('time (in minutes)')


# Label the y-axis
plt.ylabel('distance (in km)')


# Set limits for x-axis (time)
ax.set_xlim([0, 40])


# Set limits for y-axis (distance)
ax.set_ylim([0, 100])


# -----------------------------
# REFERENCE LINES
# -----------------------------


# Draw a vertical dashed line at t = 30 minutes
# Used to mark an important time point
plt.axvline(x=t_intercept, color='purple', linestyle='--')


# Draw a horizontal dashed line at distance = 75 km
# The underscore (_) means we ignore the returned object
_ = plt.axhline(y=d_intercept, color='purple', linestyle='--')


# -----------------------------
# OPTIONAL: PLOT MOTION CURVES
# -----------------------------


# Plot robber's distance vs time
ax.plot(t, d_r, label='Robber', color='red')


# Plot cop's distance vs time
ax.plot(t, d_c, label='Cop', color='blue')


# Display legend to identify lines
ax.legend()


# -----------------------------
# DISPLAY THE GRAPH
# -----------------------------


# This line is REQUIRED in VS Code (not needed in Jupyter)
# It tells Python to actually show the plot window
plt.show()
