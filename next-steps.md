Deadline: Sept 26

### Phase I: Demand-side
I would like to create a student-student graph that is able to cluster similar student interests. Then, using the definition of these clusters, I can compare how well each of the clusters are served by the existing clubs (in phase 2)

- create edge definition for similarity between students
- apply community detection algorithms (leiden algo as a start) to get a better understanding
- (ext.) use sliders to adjust the granularity of clusters formed to come to a vibe-based conclusion on the weights
- (ext.) look approximately how this is actually achieved and reach out to some people for this

### Phase II: Comparison
Now compare these formed clusters with the existing distribution of clubs. Then see which clusters are underserved and understand why this is the case. E.g.

```
Cluster 3: 14% of 58 students are connected.

Clubs pertaining to `linguistics` are sparsely distributed
The cost for a relatively niche interest is high; either through travelling or admission costs.
This leaves only a minority able to attend the club.

There could be redirections for "MFL" or "coding" clubs depending on the student's further interests. 
```

### Phase III: Interaction & Accurary
The model know allows for the interactive addition of clubs to try to respond to underserved communities, in a clear website. The base layer of this would be some OpenStreetMap wrapper and based on actual council data; using transportation connections and deprivation data to infer the edge weights. 

Using survey responses and the ability of constructing a faux-`csv` file in a manner that is similar to how I would present this to a council. 

Further iterations, would be for the conversion of a written text into a club allocation and student allocation. 

There is an inherent bias in the fact that people more-likely to complete such surveys and get involved would not necessarily be representative of the population. The final phase would be some way of inferring (or asking for) real data on people's interest -- since interest was one major reason why people did not attend local youth clubs (DCMS, 2024).

------

**Therefore, the best short-term goal for this would be map from synthetic data that can identify a cluster and present where this cluster has arrived geospatially (there can be multiple plots of this using networkx and matplotlib).**

**As an extension:**
- include the wealth of local areas (and try to understand how policy can be applied into a model)
- using a slider to change different global parameters (like data 'completeness'* or the level of austerity in the area (an area's available funding per time period))
- could there be multiple areas (there is an intention of trying to incentivise sharing of funding)

* `data-completeness` is some vague term to encode how true the data is from a given source and how much it is inferred. Hopefully, the model would be able to handle some students who have not participated in the survey (although this would be a silly thing to present so I won't).
