# T81-558: Applications of Deep Neural Networks
# Module 13: Advanced/Other Topics
# Instructor: [Jeff Heaton](https://sites.wustl.edu/jeffheaton/), McKelvey School of Engineering, [Washington University in St. Louis](https://engineering.wustl.edu/Programs/Pages/default.aspx)
# For more information visit the [class website](https://sites.wustl.edu/jeffheaton/t81-558/).
# Deploy simple Keras tabular model with Flask only.
from flask import Flask, request, jsonify
import uuid
import os
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Used for validation
EXPECTED = {
  "cylinders":{"min":3,"max":8},
  "displacement":{"min":68.0,"max":455.0},
  "horsepower":{"min":46.0,"max":230.0},
  "weight":{"min":1613,"max":5140},
  "acceleration":{"min":8.0,"max":24.8},
  "year":{"min":70,"max":82},
  "origin":{"min":1,"max":3}
}

# Load neural network when Flask boots up
model = load_model(os.path.join("../dnn/","mpg_model.h5"))

@app.route('/api/mpg', methods=['POST'])
def calc_mpg():
    content = request.json
    errors = []

    # Check for valid input fields 
    for name in content:
      if name in EXPECTED:
        expected_min = EXPECTED[name]['min']
        expected_max = EXPECTED[name]['max']
        value = content[name]
        if value < expected_min or value > expected_max:
          errors.append(f"Out of bounds: {name}, has value of: {value}, but should be between {expected_min} and {expected_max}.")
      else:
        errors.append(f"Unexpected field: {name}.")

    # Check for missing input fields
    for name in EXPECTED:
      if name not in content:
        errors.append(f"Missing value: {name}.")

    if len(errors) <1:
      # Predict
      x = np.zeros( (1,7) )

      x[0,0] = content['cylinders']
      x[0,1] = content['displacement'] 
      x[0,2] = content['horsepower']
      x[0,3] = content['weight']
      x[0,4] = content['acceleration'] 
      x[0,5] = content['year']
      x[0,6] = content['origin']

      pred = model.predict(x)
      mpg = float(pred[0])
      response = {"id":str(uuid.uuid4()),"mpg":mpg,"errors":errors}
    else:
      # Return errors
      response = {"id":str(uuid.uuid4()),"errors":errors}


    print(content['displacement'])
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)