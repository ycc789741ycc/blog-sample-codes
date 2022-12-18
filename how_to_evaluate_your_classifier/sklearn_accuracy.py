from sklearn.metrics import f1_score


prediction = [0, 1, 0, 1]
ground_truth = [0, 1, 1, 1]

score = f1_score(prediction, ground_truth)
print(score)