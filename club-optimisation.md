I want to suggest where a new club could be added to a given cluster to reduce the edge weights of it. 

### Initial approach
The new club will be a node in the set of clubs with a vector attribute $\vec{x}$ which minimises the differences between each of the relational attributes of students in the targeted cluster. 

Therefore, we would want to minimise this sum $\sum^{N}_{i}(x-S_i)^2$. Here, $S = {S_0, S_1, ..., S_n}$, the set of vector attributes of nodes within a given cluster and $N$ is just the length of this set. 

As with any function, differentiating and setting the first derivative to zero gives a stationary point. I cannot assume that the vector $\vec{x}$ will be a minimum in this form but it will be the starting point. 

To differentiate a vector function, the below steps will take place: 
$$f(\vec{x}) = \sum^{N}_{i}(x-S_i)^2, \vec{x} \in \mathbb{R}^n$$
$$\nabla f(\vec{x}) = 2\sum^{N}_{i}(x-S_i)$$

$$\nabla f(\vec{x}) = 0$$
