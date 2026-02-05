.. filepath: d:\python cpde\Kinetic_Monte_Carlo\docs\source\examples.rst
Examples
========

Basic 2D Simulation
-------------------

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from KMC import KMC1
   
   # Simulation parameters
   initial_position = [0, 0]
   gamma_1 = 0.8  # High rate for simple hops
   gamma_2 = 0.2  # Low rate for diagonal hops
   N = 5000       # Number of steps
   
   # Run simulation
   trajectory = KMC1(initial_position, gamma_1, gamma_2, N)
   
   # Visualize results
   plt.figure(figsize=(10, 8))
   plt.plot(trajectory[:, 0], trajectory[:, 1], 'b-', alpha=0.7, linewidth=0.5)
   plt.plot(trajectory[0, 0], trajectory[0, 1], 'go', markersize=10, label='Start')
   plt.plot(trajectory[-1, 0], trajectory[-1, 1], 'ro', markersize=10, label='End')
   plt.xlabel('X Position')
   plt.ylabel('Y Position')
   plt.title('2D Random Walk Trajectory')
   plt.legend()
   plt.grid(True, alpha=0.3)
   plt.axis('equal')
   plt.show()
   
   print(f"Final position: {trajectory[-1]}")
   print(f"Total displacement: {np.linalg.norm(trajectory[-1] - trajectory[0])}")

3D Lattice Simulation
---------------------

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   from KMC import KMC2
   
   # 3D simulation parameters
   initial_position = [0, 0, 0]
   gamma_1 = 0.6    # Oxygen-oxygen hopping rate
   gamma_2 = 0.4    # Complex hopping rate
   a = 2.0          # Lattice parameter
   b = 0.5          # Hopping distance
   N = 2000         # Number of steps
   
   # Run 3D simulation
   trajectory_3d = KMC2(initial_position, gamma_1, gamma_2, a, b, N)
   
   # 3D visualization
   fig = plt.figure(figsize=(12, 9))
   ax = fig.add_subplot(111, projection='3d')
   
   # Plot trajectory
   ax.plot(trajectory_3d[:, 0], trajectory_3d[:, 1], trajectory_3d[:, 2], 
           'b-', alpha=0.6, linewidth=0.8)
   
   # Mark start and end points
   ax.scatter(trajectory_3d[0, 0], trajectory_3d[0, 1], trajectory_3d[0, 2], 
              c='green', s=100, label='Start')
   ax.scatter(trajectory_3d[-1, 0], trajectory_3d[-1, 1], trajectory_3d[-1, 2], 
              c='red', s=100, label='End')
   
   ax.set_xlabel('X Position')
   ax.set_ylabel('Y Position')
   ax.set_zlabel('Z Position (Site Type)')
   ax.set_title('3D Lattice Hopping Trajectory')
   ax.legend()
   plt.show()

Performance Comparison
---------------------

.. code-block:: python

   import time
   import numpy as np
   from KMC import KMC1
   
   # Performance test
   position_0 = [0, 0]
   gamma_1, gamma_2 = 0.5, 0.5
   
   # Test different simulation sizes
   sizes = [1000, 5000, 10000, 50000]
   times = []
   
   print("Performance Analysis:")
   print("=" * 40)
   
   for N in sizes:
       start_time = time.time()
       trajectory = KMC1(position_0, gamma_1, gamma_2, N)
       end_time = time.time()
       
       duration = end_time - start_time
       times.append(duration)
       steps_per_sec = N / duration if duration > 0 else float('inf')
       
       print(f"N={N:5d}: {duration:.4f} seconds ({steps_per_sec:.0f} steps/sec)")
   
   # Plot performance
   plt.figure(figsize=(8, 6))
   plt.loglog(sizes, times, 'bo-', linewidth=2, markersize=8)
   plt.xlabel('Number of Steps (N)')
   plt.ylabel('Execution Time (seconds)')
   plt.title('KMC1 Performance Scaling')
   plt.grid(True, alpha=0.3)
   plt.show()