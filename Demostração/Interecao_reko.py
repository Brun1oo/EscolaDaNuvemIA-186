import boto3

sesseion = boto3.Session(profile_name="BRSAO186")

client = sesseion.client('rekognition', region_name='us-east-1')

response = client.detect_labels(
        Image={
            "S2Object": {
                "Bucket": "brsao-186-rekognition",
                "Name":"imagem_03.png"
            }
        }
)

for label in response["Labels"]:
    print(f"Objeto: {label['Name']}, Confiaça: {label['Confidence']: .3f}")