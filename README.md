# Malicious-Detection-Network-Security-Final-Project
## Description
The respository is used to store the code for Network Security final project. The malicious_phish.csv is the raw data set.
## Instruction
1. Use script 'multiThread_crawler.ipynb' to crawl URLs in raw dataset to check whether the URL is active and download HTML source code.
2. Use script 'URL_Feature_Process.py' continuous process dataset and add lexical and host-based features.
3. Use script 'HTMLparser.ipynb' to extract content-based features from HTML source code.
4. Use script 'hash_Process.py' make hash tables for data from last step.
5. Use script 'hash_features.py' to solve lable overlapping problem.
6. Realse comments for dropping lexical and host base features to focus on content base features.
7. Use script 'kmeans.py' to train K means model.
8. Use script 'mlp.py' to train MLP model.
9. Use script 'svm.py' to train SVM model.
10. Use script 'random_forest.py' to train random forest model.
11. Release comments for dropping content base features to focus on lexical and host base features. 
12. Back to step 6 and train again.
13. Release all comments to train the model with all features.
