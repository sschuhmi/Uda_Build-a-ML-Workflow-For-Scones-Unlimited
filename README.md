# Uda_Build-a-ML-Workflow-For-Scones-Unlimited
Udacity Project on "Build-a-ML-Workflow-For-Scones-Unlimited" (part of AWS Machine Learning Engineer Nanodegree)

This project submission contains the following contents:
- Folder "StateMachine & Lambdas": Contains the exported AWS StepFunctions State Machine as well as the 3 AWS Lambda functions - lambda1.py ("Serialize Image Data", Step 1 of the State Machine), lambda2.py ("Generate Inferences", Step 2 of the State Machine) and lambda3.py ("Threshold-based Filtering", Step 3 of the State Machine)
- Folder "StateMachine Screenshots&Exports": Contains 3 screenshots of the State Machine´s Executions - two successful executions, performed by with bike and a motorcycle image from the test folder, and an execution which led to a failure since the threshold condition (max(inferences)>0.93) was not met. This execution was performed with the image of a cow which was also used as example in the Jupyter Notebook
- Folder "captured_data": Contains the jsonl files created for the State Machine executions, i.e. Model Monitor data extraction used for visualization. These are the foundation for the graphical illustrations at the end in the Jupyter Notebook.
- LICENSE: An auto-generated license file
- README.md: This document
- bicycle_s_000513.png: The exemplary image of a bike from the test folder which was used for a successful State Machine execution, leading to an inference of >0.93 for the condition being a bike.
- file.png: The exemplary image of a cow from the test folder which was used for a State Machine execution leading to a failure, since the threshold condition was obviously not met for the cow image.
- motorbike_s_000433.png: The exemplary image of a motorcycle from the test folder which was used for a successful State Machine execution, leading to an inference of >0.93 for the condition being a motorcycle.
- starter.ipynb: The completed Jupyter Notebook which contains all code sources, especially the Lambda functions and the completed code for the visualizations (at the end).
- test.lst: The list of images which have been regarded for testing the model´s performance
- train.lst: The list of images which have been regarded for training the model
