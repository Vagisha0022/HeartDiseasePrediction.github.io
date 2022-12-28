import numpy as np
import pickle
loaded_model =pickle.load(open('trained_model.sav','rb'))
input_data = (52,1,0,125,212,0,1,168,0,1,2,2,3)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not having a heart disease')
else:
  print('The person is having a heart disease')
                         