import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Make a random walk
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    #Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16, 9))

    point_numbers = range(rw.num_points)
    #normalized_point_numbers = [(p - min(point_numbers)) / (max(point_numbers) - min(point_numbers)) for p in point_numbers]

    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect('equal')

    #Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=60)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=60)

    #Remove the axes

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #x_y_pairs = zip(rw.x_values, rw.y_values)
    #x_y_dict = dict(x_y_pairs)
    #for x, y in x_y_dict.items():
    #    print(f"{x} and {y}")
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break