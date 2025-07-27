
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import numpy as np

# Example true and predicted labels
y_true = np.array(['fast', 'medium', 'slow', 'medium', 'fast'])
y_pred = np.array(['fast', 'slow', 'slow', 'medium', 'medium'])

precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')
conf_matrix = confusion_matrix(y_true, y_pred, labels=['fast', 'medium', 'slow'])

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
