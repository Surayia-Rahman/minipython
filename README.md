This is a bunch of university small projects catering to different aspects. The description are as below:

1. FLP assignment (Functional and Logical Programming):

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
