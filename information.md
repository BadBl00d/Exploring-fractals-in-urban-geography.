## Introduction

Since the 1960s, graph theory has been used to describe telecommunication networks and data flows. However, distinguishing between two very similar graphs that represent vastly different "territorial" realities or accounting for angles and spatial terrain disposition proves challenging. Urban development often results in the emergence of an amorphous and fragmented cityscape, even when the initial city planning was conceived with regular geometry.

For about three decades now, geographers have been intrigued by fractal geometry, following the pioneering work of Benoît Mandelbrot (1977). Numerous applications of fractals in our discipline have been explored, but no other area has been as extensively examined by fractal geographers as that of the city. Michael Batty and Paul Longley are arguably the first authors to delve into the applications of fractals in this field. In the mid-1980s, they began studying the fractality of urban structures with the aim of better simulating the growth of these entities (Batty and Longley, 1986). A few years later, Pierre Frankhauser published a more general synthesis of what could be expected from fractal geometry in urban geography (Frankhauser, 1991).

2/ Fractals: Definition and Characteristics

Differentiable curves lack this property. Upon closer examination of a differentiable curve, after a few enlargements, the portion of the curve appears straight (in fact, it eventually coincides with its tangent near the point being observed).

Similarity dimension: dimension obtained through an evaluation of degrees of freedom (number of pieces of information needed to locate a point).
Dilation factor s -> we will have N = sd

Example: von Koch curve.

Curve dimensions (more detailed in the appendix): We limit ourselves here to simple curves in the plane (or space), i.e., without multiple points.

Box-counting dimension: We assume that this is the simplest to calculate and comes closest to the Hausdorff dimension.

Description of the principle: counting boxes containing a black pixel and logarithmic linear regression.
England's Coastline: Dc was already obtained ≃ 1.3 using the compass spacing dimension definition (described in the appendix).

3/ The City as a Fractal

Indeed, the city as a whole exhibits a certain similarity with smaller parts of itself. In this sense, the urban fabric seems to consist of an interweaving of neighborhoods, blocks, buildings... By adopting a geometric approach, we can understand how cities are structured, grow, and evolve.

As you can see, Milan has a fractal dimension of 1.85, while Stuttgart's is 1.80. We will return to the interpretation of this later.

Brief equipment detail
Principle of the box-counting algorithm: the box-counting algorithm is based on dividing an image into boxes of size epsilon: we obtain sub-arrays of len epsilon. We then count the number of boxes containing zero elements (black pixels) before plotting the points. If the box sizes match, i.e., if we count enough points, we move on to linear regression; otherwise, we decrease the box size. We then draw as per the graph.

For this, I developed two algorithms (in two steps). The first one works directly on arrays and, with the help of a function is_black(image: PIL type, epsilon: int type): int, traverses the image with a given box size. Then we go through an array of boxes. It has a complexity of O(n^3). This algorithm gave convincing but inaccurate results initially. Moreover, its complexity did not make it effective over time.

Compare time arrays

The second algorithm developed is more efficient as it contains only double loops (two nested loops) and relies on the use of numpy arrays and notably the np.histogramdd function.

Array: comparison of the two:
-Sierpinski triangle: 1.58
-Sierpinski carpet: 1.89
-Filled plane: 2

A simple deviation calculation confirms the relevance of the model when applied to simple figures.

Confirmation of the model: what is found in the literature:

Values obtained in a study conducted by the city of Strasbourg. For this, I developed a program using the Tkinter library. This program divides an image such as a map into boxes (here boxes of 900m) and applies the box-counting algorithm in these boxes to isolate certain neighborhoods.

The obtained values align well with the model outlined in red above.

The structure of the Strasbourg metropolitan area, our reference study area, is generally mononuclear with nuances related to the geopolitical reality of Strasbourg. A cursory observation (Figure 1) suggests a city center that traditionally developed along its outskirts and by crossing the Rhine; One of the peculiarities of the Strasbourg metropolitan area is therefore its cross-border character. From the center to the periphery, three main phases of urbanization can be read in its built fabric.

Firstly, the central artificial island, ovoid in shape, which encompasses most of the medieval city of Strasbourg. The built fabric of this space has been profoundly restructured over the centuries: some places retain a medieval aspect.
-The second noteworthy area in terms of urban fabric is the Neustadt, i.e., the extension of the city over the razed fortifications of Vauban.
-Outside this green belt are the peri-central neighborhoods, the former outskirts of the city, as well as former towns or villages previously peri-urban, including the city of Kehl, which have been caught up in the development of the metropolis.
A second approach given in the literature is the dilation dimension.

Algorithm: The dilation analysis transforms the structure by gradually making its details disappear. Here, each black pixel, occupied, is replaced by a black square of size e, centered on the pixel. These squares are gradually dilated. The voids separating the occupied parts gradually disappear; on the other hand, increasingly extensive aggregates form and join together during the dilation steps.

However, preliminary investigations have shown that this method is less reliable. Indeed, the counting algorithm also takes into account the mass of black pixels that are added by dilating the original structure. Thus, the mass of occupied points tends to be overestimated. This phenomenon affects more the structures whose occupied mass is initially low, such as linear objects, because the relative error is then greater. The use of this method will therefore be limited to calculating fractal dimensions on surfaces.

4/ Practical Application to the City of Paris

In the first instance, I focused on the study of continuous fabric. Thanks to the maps provided by Copernicus Land and a quick image processing, we can recreate a map of Paris and its suburbs. On the maps above, we can observe the fractal dimension as well as the extent of Paris and its suburbs at different times.

Facts: The urban unit of Paris includes 10.7 million inhabitants. Over the past decades, the most positive dynamics have been observed not in the heart of the Parisian agglomeration but in its surroundings. Apart from congestion problems, this situation of decentralization from the capital results notably from deliberate planning choices that began in the 1960s, such as the policy of new cities or the commissioning of the RER. Thus, the growth of employment and population within Paris and its inner suburbs has been on average more than five times lower than in the rest of Île-de-France between 1975 and 2015.

The fractal dimension therefore effectively models urban planning and the development of the urban fabric. Let's conduct a more detailed analysis: we apply the program obtained earlier to Paris to obtain an average value of 1.81, comparable to large European cities with similar architecture and layout.

Although less relevant, I applied the dilation algorithm to five districts of the capital, each housing different attractions (e.g., 16th rather residential + Bois de Boulogne // 5th where almost all buildings are pre-1950, therefore dense).

In a third step, I calculated the dimension of these districts with software developed by Gilles Vuidel at the ThéMA laboratory (CNRS Besançon).

Explain the dimension specific to each district: Discussion of local results, for typical fabrics:

The high tortuosity of the central districts is explained by the particular morphology of the built environment, which consists of large blocks several hundred meters long at times. The streets, constrained to bypass these blocks, tend to cause the elongation of routes.

These districts, made up of large blocks and vast blocks, by lengthening the routes, therefore favor motorized travel at the expense of nearby pedestrian travel.

Comparison with other geographical indicators:

It is not my intention to carry out a detailed study aiming to confront this indicator with other indicators resulting from spatial analysis, however:
-density:
The results converge with the calculation carried out by the IAU IDF in the 6th arrondissement, which shows a built density of 4. This district is characterized by the presence of Haussmannian buildings with an average height of 6 floors and a footprint of 75%.

Knowing that the built density of an individual housing operation is around 0.3, that of the large complexes in La Courneuve is 0.75, and that of traditional "townhouses" is 1 (source: IAU).

5/ Limitations and Perspectives

However, some limitations to this model can be mentioned:
Dilatation: For this method, it is interesting to see how many steps are necessary for different types of fabrics to form a single aggregate with a well-defined border. This number will necessarily be different depending on whether we are in a historic city center or in a recent peripheral zone: it gives an indication of the size of the spaces between buildings. This indication will allow us to develop an initial classification of morphological differences in the tissues analyzed, relying on a measure that is not strictly speaking fractal.

Notable exception: the Hautepierre district is the morphological unit where the aggregation threshold is reached the latest.
