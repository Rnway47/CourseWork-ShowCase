import matplotlib.pyplot as plt
import numpy as np
import os
### Q6 cell, this is done in Jhub

pos_folder_path = "CSC 421/pos/" #change the folder path if different than yours
neg_folder_path = "CSC 421/neg/" #change the folder path if different than yours
pos_file = os.listdir(pos_folder_path)
neg_file = os.listdir(neg_folder_path)
#read each file and make it for transforming it to binary vector, start with the pos folder
pos_list = []
for file in pos_file:
    f = open(pos_folder_path+file, "r")
    pos_list.append(f.read())
    
#convert it to binary vector
keywords = ["awful", "bad", "boring", "dull", "effective", "enjoyable", "great", "hilarious"]
pos_vector = []
for item in pos_list:
    binary_vector = np.zeros(len(keywords))
    for index in range(len(keywords)): #search if any keywords exist, replace 0 with 1 if it does
        if keywords[index] in item:
            binary_vector[index] = 1
    pos_vector.append(binary_vector)
#do the same for neg folder
neg_list = []
for file in neg_file:
    f = open(neg_folder_path+file, "r")
    neg_list.append(f.read())
    
neg_vector = []
for item in neg_list:
    binary_vector = np.zeros(len(keywords))
    for index in range(len(keywords)): #search if any keywords exist, replace 0 with 1 if it does
        if keywords[index] in item:
            binary_vector[index] = 1
    neg_vector.append(binary_vector)

pos_prob = (np.add.reduce(pos_vector) + 1) / (len(pos_vector)+ 1) #adding 1 in case none of these words are present
neg_prob = (np.add.reduce(neg_vector) + 1) / (len(neg_vector)+ 1)
print("Among positive reviews, the probability of each word is present")
for index in range(len(pos_prob)):
    print(f"{keywords[index]}:  {pos_prob[index]}")
print("\nAmong negative reviews, the probability of each word is present")
for index in range(len(neg_prob)):
    print(f"{keywords[index]}:  {neg_prob[index]}")

### Q7 cell, this is done in Jhub

def likelihood(test_review, word_prob_for_type): 
    probability_product = 1.0 
    for (i, w) in enumerate(test_review): 
        if (w == 1): 
            probability = word_prob_for_type[i]
        else: 
            probability = 1.0 - word_prob_for_type[i]
        probability_product *= probability 
    return probability_product

def predict(test_review): 
    scores = [likelihood(test_review, pos_prob), 
             likelihood(test_review, neg_prob)]
    labels = ['positive', 'negative']
    return labels[np.argmax(scores)]

review_index = np.random.randint(1000)
print("Random positive review's index", review_index)
test_review = pos_vector[review_index]
print(predict(test_review))

#Q8 cell, this is done in Jhub

# we will take 90% of the samples (1800 reviews) as training set, the rest 10% (200 reviews) for testing set, training set evaluation first
#shuffle each list and take the first 900 of each list as training samples
import random
random.shuffle(pos_vector)
random.shuffle(neg_vector)
train_set = pos_vector[0:900] + neg_vector[0:900]
test_set = pos_vector[900:1000] + neg_vector[900:1000]
train_truth_label = ["positive" if x < 900 else "negative" for x in range(1800)]
test_truth_label = ["positive" if x < 100 else "negative" for x in range(200)]
#evaluation part: accuracy with confusion matrix
def predict_set(test_set, ground_truth_label):
    TP = 0 # number of true positives
    FN = 0 # number of false negatives
    TN = 0 # number of true negatives
    FP = 0 # number of false positives
    for index in range(len(test_set)): 
        if predict(test_set[index]) == "positive": #predicted as positive class
            if predict(test_set[index]) == ground_truth_label[index]:
                TP += 1 #true positive detected, same as ground truth label
            else:
                FN += 1 #should be negative but detected as positive
        else: #predicted as negative class
            if predict(test_set[index]) == ground_truth_label[index]:
                TN += 1 #true negative detected, same as ground truth label
            else:
                FP += 1 #should be positive but detected as negative
    acc = (TP+TN) / (TP+FN+TN+FP) #classification accuracy
    confusion_matrix = np.array([[TP, FP], [TN, FN]])
    print(f"Accuracy of the classifier: {acc}")
    print(f"Confusion Matrix of the classifier: {confusion_matrix}") #due to the formatting, the matrix would look a bit off but the values are correct

print("Evaluation of the training set")
predict_set(train_set, train_truth_label)
print("Evaluation of the test set")
predict_set(test_set, test_truth_label)