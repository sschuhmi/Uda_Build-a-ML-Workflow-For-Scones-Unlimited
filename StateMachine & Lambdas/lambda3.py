import json


THRESHOLD = .93


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences = json.loads(event["inferences"]) #[float(value) for value in event["inferences"]]

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(inference > THRESHOLD for inference in inferences) ## TODO: fill in
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        print("THRESHOLD ",THRESHOLD, " WAS MET BY INFERENCE ", inferences)
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }