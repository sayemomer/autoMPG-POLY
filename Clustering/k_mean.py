import numpy as np
import matplotlib.pyplot as plt

# Generating a sample dataset
np.random.seed(42)
X = np.random.rand(10,2) * 10  # 10 points in 2D space

# Initial centroids based on points A and B
C1 = np.array([3.75, 9.51])  # Centroid 1
C2 = np.array([7.32, 5.99])  # Centroid 2

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def update_centroids(X, assignments):
    cluster1 = X[assignments == 0]
    cluster2 = X[assignments == 1]
    C1_new = np.mean(cluster1, axis=0) if cluster1.size else C1
    C2_new = np.mean(cluster2, axis=0) if cluster2.size else C2
    return C1_new, C2_new

# Initialize plot
plt.ion()  # Turn on interactive mode
figure, ax = plt.subplots(figsize=(8, 6))

for iteration in range(10):  # Limit the iterations to prevent infinite loop
    assignments = np.zeros(X.shape[0])
    for i, point in enumerate(X):
        distance_to_C1 = euclidean_distance(point, C1)
        distance_to_C2 = euclidean_distance(point, C2)
        assignments[i] = 0 if distance_to_C1 < distance_to_C2 else 1
    
    # Clear the previous plot
    ax.clear()
    
    # Plot data points and centroids with current assignments
    ax.scatter(X[:, 0], X[:, 1], c=assignments, cmap='viridis', marker='o', label='Data Points')
    ax.scatter([C1[0], C2[0]], [C1[1], C2[1]], c='red', s=200, alpha=0.5, marker='X', label='Centroids')
    plt.title(f'K-means Clustering Iteration {iteration+1}')
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.legend()
    plt.grid(True)
    plt.pause(0.1)  # Pause to visualize update
    
    # Update centroids
    C1_new, C2_new = update_centroids(X, assignments)
    
    # Check for convergence
    if np.allclose(C1, C1_new) and np.allclose(C2, C2_new):
        print(f"Converged after {iteration+1} iterations")
        break
    
    C1, C2 = C1_new, C2_new

plt.ioff()  # Turn off interactive mode
plt.show()
