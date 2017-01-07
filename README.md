# Machine Learning Recipes
Repo for Machine Learning Recipes with Josh Gordon from Google

Recipes were made with:
- Anaconda 4.2.0
- Python 2.7.12
- pydot 1.2.2
- graphviz 2.38.0 (Tip: on Windows add directory with dot.exe (in my case ...\Anaconda2\Library\bin\graphviz) to Path environment variable)

## Notes

#### Recipe #1

Supervised Learning Recipe consists of:

```Collect Training Data -> Train Classifier -> Make Predictions```

#### Recipe #2

Testing Data are examples used to "test" the classifier's accuracy (not part of the training data).

#### Recipe #3

Features should capture different types of information. Independent and easy to understand features are best.

Avoid useless and redundant features.

#### Recipe #4

Classifier is a function ```f(x) = y``` where f(x) represents features and y is label.

#### Recipe #5

KNN (K nearest neighbor) is based on minimum distance (for example Euclidean distance) from the query instance to the training
samples to determine the K-nearest neighbors. After you gather K nearest neighbors, you take simple majority of these
K-nearest neighbors to be the prediction of the query instance.

Pros:

- relatively simple,

- working well for some problems.

Cons:

- computationally intensive,

- hard to represent relationships between features.

#### Recipe #6

All required ingredients for this recipe you can find on https://codelabs.developers.google.com/codelabs/tensorflow-for-poets

Deep learning works on raw pixels from image so you not need to extract features manually.

Retraining also known as Transfer Learning leverages prior work and use previously trained model (in our case 'Inception').

Clue for image classifier are diversity and quantity, which mean we should have a lot of different images in each category.
