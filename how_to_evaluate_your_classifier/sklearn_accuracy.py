from sklearn.metrics import accuracy_score


prediction = [0, 1, 0, 1]
ground_truth = [0, 1, 1, 1]

score = accuracy_score(prediction, ground_truth)
