# Animating the ForceAtlas2 algorithm

| Straight edges | Curved edges |
|---|---|
| <img src="https://github.com/beyondbeneath/animate-forceatlas2/blob/master/anim-straight.gif" height=300px> | <img src="https://github.com/beyondbeneath/animate-forceatlas2/blob/master/anim-curved.gif" height=300px> |

This script leverages a [modification](https://github.com/bhargavchippada/forceatlas2/pull/11) of the [`fa2` Python package](https://github.com/bhargavchippada/forceatlas2), which allows the historical positions of the nodes (while the algorithm is iterating) to be returned. The (NetworkX) graph at each stage can then simply be visualised, and therefore animated.

## Dependencies

* You will need to first clone the branch of my `fa2` PR by the following command: `git clone https://github.com/beyondbeneath/forceatlas2.git -b maintain-position-history /path/to/fa2-anim`

* If you wish to plot aesthetic Bezier edges, you should copy the function available in the [`bezier-curved-edges-networkx`](https://github.com/beyondbeneath/bezier-curved-edges-networkx) repo.

* [NetworkX](https://networkx.github.io/): `networkx==2.2`

## Sample usage

For this example, I will re-use the Game of Thrones network I gave in the [`bezier-curved-edges-networkx`](https://github.com/beyondbeneath/bezier-curved-edges-networkx) repo, but this will run on any NetworkX graph, represented here by the object `G`.

All we do here is setup a `ForceAtlas2` function with appropriate parameters, and then run the `animate_fa2` function:

```python
f = ForceAtlas2(seed=100,
                outboundAttractionDistribution=True,
                edgeWeightInfluence=0,
                gravity=1,
                scalingRatio=10,
                verbose=False)

animate_fa2(G, f, num_iterations=100, output_dir='/tmp/fa2', edge_type='straight')
```

This will output `num_iterations` frames to `/tmp/fa2`. If you choose anything other than `edge_type='straight'` it will attempt to use the [curved edges](https://github.com/beyondbeneath/bezier-curved-edges-networkx) function that you will need to have in the same file. All the node & edge formatting are hard-coded in the function, but can be easily modified.

From here, you can combine the frames into an animated gif using your favourite tool. For example, using [ImageMagick convert tool](https://imagemagick.org/script/convert.php) on MacOS:

```
convert -delay 10 anim_frame_* animation.gif
```
