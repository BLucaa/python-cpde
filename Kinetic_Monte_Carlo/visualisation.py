#%%
import numpy as np
import sys
sys.path.insert(0, r'd:\python cpde\Kinetic_Monte_Carlo')
from KMC import KMC1, KMC2
import matplotlib.pyplot as plt
#%%
class KMCVisualizer:
    """
    A class for visualizing Kinetic Monte Carlo simulation results.
    """
    
    def __init__(self, figure_size=(8, 8)):
        """
        Initialize the visualizer.
        
        Args:
            figure_size (tuple): The size of the matplotlib figure (width, height).
        """
        self.figure_size = figure_size
    
    def visualize_kmc(self, trajectory, title='KMC Simulation Results'):
        """
        Visualizes the results of KMC simulations.

        Args:
            trajectory (np.ndarray): The trajectory data from KMC1 or KMC2.
            title (str): The title of the plot.
        """
        plt.figure(figsize=self.figure_size)
        plt.plot(trajectory[:, 0], trajectory[:, 1], marker='o', linestyle='-', markersize=3)
        plt.title(title)
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.xlim(np.min(trajectory[:, 0]) - 1, np.max(trajectory[:, 0]) + 1)
        plt.ylim(np.min(trajectory[:, 1]) - 1, np.max(trajectory[:, 1]) + 1)
        plt.grid()
        plt.axis('equal')
        plt.show()
        
    def visualize_kmc_grid(self, trajectory, lattice_constant, title='KMC Simulation Results'):
        """
        Visualizes KMC trajectory on a square lattice grid.

        Args:
            trajectory (np.ndarray): The trajectory data from KMC1 or KMC2.
            lattice_constant (float): The spacing between lattice points.
            title (str): The title of the plot.
        """
        plt.figure(figsize=self.figure_size)
        
        # Plot lattice grid
        x_min, x_max = np.min(trajectory[:, 0]) - 1, np.max(trajectory[:, 0]) + 1
        y_min, y_max = np.min(trajectory[:, 1]) - 1, np.max(trajectory[:, 1]) + 1
        
        x_grid = np.arange(x_min, x_max + lattice_constant, lattice_constant)
        y_grid = np.arange(y_min, y_max + lattice_constant, lattice_constant)
        
        for x in x_grid:
            plt.axvline(x, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
        for y in y_grid:
            plt.axhline(y, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
        
        # Plot trajectory
        plt.plot(trajectory[:, 0], trajectory[:, 1], marker='o', linestyle='-', markersize=3, color='blue')
        plt.title(title)
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.grid(False)
        plt.axis('equal')
        plt.show()
    
    def visualize_kmc2_with_grid(self, trajectory, a, b, title='KMC2 Simulation with Grid Nodes'):
        """
        Visualizes KMC2 trajectory with red dots on grid nodes.
        
        Args:
            trajectory (np.ndarray): The trajectory data from KMC2 (N x 3 array).
            a (float): Parameter 'a' used in KMC2.
            b (float): Parameter 'b' used in KMC2.
            title (str): The title of the plot.
        """
        plt.figure(figsize=self.figure_size)
        # Get trajectory bounds with some padding
        x_min = np.min(trajectory[:, 0]) 
        print(x_min)
        x_max = np.max(trajectory[:, 0]) 
        y_min = np.min(trajectory[:, 1]) 
        y_max = np.max(trajectory[:, 1]) 
        
        # Create grid of potential lattice sites
        # For KMC2, the lattice spacing is related to parameters a and b
        lattice_spacing = a
        x_nodes =  np.concatenate([np.arange(0,x_min-lattice_spacing , lattice_spacing),
                                 np.arange(0, x_max + lattice_spacing, lattice_spacing)])
        y_nodes = np.concatenate([ np.arange(0,y_min-lattice_spacing , lattice_spacing),
                                 np.arange(0, y_max + lattice_spacing, lattice_spacing)])
        
        # Plot red dots on all grid nodes
        for x in x_nodes:
            for y in y_nodes:
                plt.plot(x, y, 'ro', markersize=5, alpha=0.6)
        
        # Plot the trajectory
        plt.plot(trajectory[:, 0], trajectory[:, 1], 'b-', linewidth=2, alpha=0.8, label='Trajectory')
        plt.scatter(trajectory[:, 0], trajectory[:, 1], c=trajectory[:, 2], cmap='viridis', 
                   s=30, edgecolors='black', linewidth=0.5, label='Visited sites', zorder=5)
        
        # Mark start and end points
        plt.plot(trajectory[0, 0], trajectory[0, 1], 'go', markersize=8, label='Start', zorder=6)
        plt.plot(trajectory[-1, 0], trajectory[-1, 1], 'ro', markersize=8, label='End', zorder=6)
        
        plt.title(title)
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        
        # Add colorbar to show site types
        cbar = plt.colorbar(plt.scatter([], [], c=[], cmap='viridis'))
        cbar.set_label('Site Type')
        
        plt.show()
    
    def visualize_kmc2_sites_only(self, trajectory, a, b, title='KMC2 Site Types'):
        """
        Visualizes only the sites visited in KMC2 simulation with different colors for each site type.
        
        Args:
            trajectory (np.ndarray): The trajectory data from KMC2 (N x 3 array).
            a (float): Parameter 'a' used in KMC2.
            b (float): Parameter 'b' used in KMC2.
            title (str): The title of the plot.
        """
        plt.figure(figsize=self.figure_size)
        
        # Define colors for different site types
        site_colors = {0: 'red', 1: 'blue', 2: 'green', 3: 'orange'}
        site_labels = {0: 'Site Type 0', 1: 'Site Type 1', 2: 'Site Type 2', 3: 'Site Type 3'}
        
        # Plot trajectory points colored by site type
        for site_type in np.unique(trajectory[:, 2]):
            mask = trajectory[:, 2] == site_type
            plt.scatter(trajectory[mask, 0], trajectory[mask, 1], 
                       c=site_colors[int(site_type)], label=site_labels[int(site_type)], 
                       s=50, alpha=0.7, edgecolors='black', linewidth=0.5)
        
        # Draw connecting lines
        plt.plot(trajectory[:, 0], trajectory[:, 1], 'k--', alpha=0.3, linewidth=1)
        
        # Mark start and end points
        plt.plot(trajectory[0, 0], trajectory[0, 1], 'ko', markersize=10, 
                markerfacecolor='white', markeredgewidth=2, label='Start')
        plt.plot(trajectory[-1, 0], trajectory[-1, 1], 'ks', markersize=10, 
                markerfacecolor='white', markeredgewidth=2, label='End')
        
        plt.title(title)
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.show()
    
    
# Example usage:
if __name__ == "__main__":
    # Create visualizer instance
    visualizer = KMCVisualizer(figure_size=(10, 8))
    b=1 #lattice constant for H
    a=4#lattice constant for O 
    # Generate trajectories
    trajectory_kmc1 = np.array(KMC1([0, 0], 0.5, 0.5, 1000))
    trajectory_kmc2 = np.array(KMC2([0, b, 0], 1/2, 1/2, a, b, 200))
    
    # Visualize individual trajectories
    #visualizer.visualize_kmc(trajectory_kmc1, title='KMC1 Simulation')
    #visualizer.visualize_kmc_grid(trajectory_kmc2, b, title='KMC2 Simulation')
    
    # Visualize KMC2 with red dots on grid nodes
    visualizer.visualize_kmc2_with_grid(trajectory_kmc2, a, b, title='KMC2 with Grid Nodes')
    
    # Visualize KMC2 sites only (color-coded by site type)
    #visualizer.visualize_kmc2_sites_only(trajectory_kmc2, a, b, title='KMC2 Site Types')
    
    