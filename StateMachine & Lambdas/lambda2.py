import json
import boto3
import base64

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2026-01-26-12-35-53-673' ## TODO: fill in

# Since zip uploading of SageMaker SDK did not work, using boto3 SageMaker runtime:
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"])

    # Directly invoke the ENDPOINT via runtime:
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image
        )
    
    # We return the data back to the Step Function    
    event["inferences"] = response['Body'].read().decode('utf-8')
    
    #print("Event:", event)

    return event