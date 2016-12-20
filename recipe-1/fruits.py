from sklearn import tree
# Fruits classifier

fruits = {0: "apple", 1: "orange"}
textures = {0: "bumpy", 1: "smooth"}

features = [[140, 1],
            [130, 1],
            [150, 0],
            [170, 0]] # [weight (g), texture]

labels = [0,
          0,
          1,
          1] # [fruit]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

fruits_to_classified = [[160, 0],
                        [100, 1]]

predicted_fruits_labels = clf.predict(fruits_to_classified)

for idx, predicted_fruit_label in enumerate(predicted_fruits_labels):
    fruit_data = fruits_to_classified[idx]
    texture = textures[fruit_data[1]]
    weight = fruit_data[0]
    predicted_fruit = fruits[predicted_fruit_label]
    print '{} {}g fruit was classified as {}'.format(texture, weight, predicted_fruit)

