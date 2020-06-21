import boto3
personalize = boto3.client('personalize')
response = personalize.create_event_tracker(
    name='Interaction-Tracker',
    datasetGroupArn='arn:aws:personalize:ap-northeast-2:027405227226:dataset-group/Cocktail-dsgroup'
)
print(response['eventTrackerArn'])
print(response['trackingId'])