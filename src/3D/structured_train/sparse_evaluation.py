'''
Plots an ROC curve combining all the prediction results.
Should be run after 'sparse_prediction.py', as that creates all the results
This script just loads them and plots them
'''

import yaml
import numpy as np
import scipy.io
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as pl
import os.path
import paths

# loading all the model results
all_models = yaml.load(open(paths.model_config, 'r'))
predictions = []

for modeloption in all_models:
	result_path = paths.results_folder + modeloption['name'] + '.mat'
	if os.path.isfile(result_path):
		print "Loading " + result_path
		this_result = scipy.io.loadmat(result_path)
		this_result['name'] = modeloption['name']
		predictions.append(this_result)
	else:
		print "Skipping " + result_path

print "In total there are : " + str(len(predictions))

# sorting by their auc
all_auc = [pred['roc_auc'] for pred in predictions]
print "AUC = " + str(np.array(all_auc).flatten())
sort_index = np.argsort(np.array(all_auc).flatten())
print "Sorted = " + str(sort_index)

# Plot ROC curve for the models
pl.clf()
for idx in sort_index[::-1]:
	pred = predictions[idx]
	label = pred['name'] + ' (area = %0.2f)' % pred['roc_auc']
	pl.plot(pred['fpr'].flatten(), pred['tpr'].flatten(), label=label)
	
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.legend(loc="lower right") 
#pl.show()
pl.savefig('plots/roc.pdf')
