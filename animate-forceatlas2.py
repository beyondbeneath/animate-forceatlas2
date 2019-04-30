import sys
sys.path.insert(0, '/path/to/fa2-anim')
from fa2 import ForceAtlas2

import os
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import networkx as nx

def animate_fa2(G, f, num_iterations=10, output_dir='/tmp', edge_type='straight'):

    # Run FA2 and store the historical positions
    historical_positions = f.forceatlas2_networkx_layout(G,
                                                         pos=None,
                                                         iterations=num_iterations,
                                                         keep_history=True)

    # Find the plot limits
    # This allows a fixed x,y axis so the animation doesn't continuously rescale
    all_positions = []
    for positions in historical_positions:
        for node_id in positions:
            all_positions.append(positions[node_id])
    all_positions = np.array(all_positions)
    xmin, ymin = all_positions.min(axis=0)
    xmax, ymax = all_positions.max(axis=0)
    
    # Plot
    num_zeros = len(str(num_iterations))
    i = 0
    plt.ioff() # Incase you're running in a notebook, this will stop it displaying n plots
    for positions in historical_positions:
        plt.figure(i, figsize=(10,10))
        plt.gca().set_facecolor('k')
        
        # Draw straight line edges
        if edge_type == 'straight':
            nx.draw_networkx_edges(G, positions, width=1, edge_color='w', alpha=0.1)
        
        # Draw curved lines ala Gephi - see https://github.com/beyondbeneath/bezier-curved-edges-networkx
        else:
            curves = curved_edges(G, positions, polarity='fixed')
            lc = LineCollection(curves, color='w', alpha=0.1)
            plt.gca().add_collection(lc)
        
        # Draw nodes and finish up
        nx.draw_networkx_nodes(G, positions, node_size=1, node_color='w')
        plt.tick_params(axis='both',which='both',bottom=False,left=False,labelbottom=False,labelleft=False)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plot_filename = 'anim_frame_{}.png'.format(str(i).zfill(num_zeros))
        plt.savefig(os.path.join(output_dir, plot_filename), bbox_inches='tight')
        plt.close()

        # Increment plot counter
        i += 1