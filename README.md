This is a bunch of university small projects catering to different aspects. The description are as below:

First and foremost, the FLP assignment (Functional and Logical Programming):

   This project simulates the creation and analysis of a system log file. It performs the following key tasks:

 a) Log File Generation:
 
A fake log file is automatically created with 1000 entries. Each entry includes a timestamp, log level (INFO, ERROR, WARNING, or DEBUG), and a message based on the log level.

 b) Data Extraction and Processing:
 
The log file is read and parsed to extract timestamps, log levels, and message content. The script calculates:

  - The number of log entries per hour (24-hour breakdown)

  - The number of entries for each log level

  - The average length of log messages

 c) Data Visualization:
 
The extracted data is visualized using bar charts, a pie chart, and a histogram:

  - Log activity by hour

  - Distribution of log levels

  - Distribution of message lengths

Result Summary:

At the end, the average length of the log messages is printed for quick insight into message verbosity.

✅ Functional Programming Perspective

1) The project simulates and analyzes log data using a functional programming mindset by emphasizing:

2) Pure Functions: Each function (e.g., generating messages, extracting info) performs a specific task with predictable outputs and no side effects.

3) Data Transformation: The program processes data through mapping and transformations, rather than altering it in-place.

4) Immutability: Variables like log entries and counts are created fresh at each stage, without mutating global state.

5) Composability: Small reusable functions are composed together to form the full workflow—from reading logs to generating statistics and plotting.

Overall, the program demonstrates clean, declarative, and stateless design, which aligns with functional programming principles.

🔍 Logical Programming Perspective

From a logical programming point of view, the project could be viewed as:

1) A collection of facts: Each log line (timestamp, log level, message) represents a structured fact in the system.

2) Rule-based reasoning: One could define rules to infer patterns, such as detecting peak log hours or high error rates.

3) Declarative intent: Instead of detailing how to calculate stats, you can express what conditions or patterns you're interested in (e.g., “Find hours with more than 50 warnings”).

4) Inference and querying: The data could be queried for specific conditions or used to derive insights through logical relationships.

Thus, in the logical paradigm, the project becomes about defining relationships and extracting knowledge from structured facts.


   The second one we'll be talking about is the mlp model for regression task. This code demonstrates how to use a Multilayer Perceptron (MLP) Regressor for regression tasks, a machine learning technique commonly used for approximating complex functions.

1) Data Generation:

Synthetic data is generated by creating random values for the feature X (between 0 and 5), and the target values y are calculated as the sine of X with some added noise. This introduces variability, simulating real-world data.

2) Model Creation:

An MLP model is created using the MLPRegressor class from scikit-learn. The model has two hidden layers, one with 100 neurons and the other with 50 neurons, which is typically used for learning non-linear relationships in data. The model is configured to run for a maximum of 1000 iterations to ensure convergence.

3) Model Training:

The model is trained by fitting it to the generated data (X, y). During training, the model adjusts its internal weights to minimize the error between the predicted outputs and actual target values (y).

4) Prediction:

After training, the model is used to predict values (y_pred) for new input data points (x_new), ranging from 0.0 to 5.0.

5) Visualization:

The training data points (X, y) and the model's predicted regression line (y_pred) are plotted on a graph. This helps visualize how well the model has learned the underlying sine function despite the added noise.

Key Points:

The MLPRegressor is a neural network-based regression model that can learn complex patterns in data.

The model is trained using a dataset that mimics a noisy sine wave, and after training, it can predict continuous values for new inputs.

The result is visualized with a plot showing both the actual noisy data and the regression line fitted by the model.

In conclusion, this code showcases the use of a neural network for regression to approximate a non-linear function, and its effectiveness can be evaluated by the accuracy of the fitted line compared to the true underlying function (sine wave).
