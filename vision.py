google.cloud import vision
from google.cloud import storage
from google.cloud.vision_v1 import ImageAnnotatorClient
from google.cloud.vision_v1 import types
from google.cloud.vision_v1.types import image_annotator
import os
import json
import numpy as np
from google.cloud import vision_v1
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"GoogleYelpDemo.json
# Get GCS bucket
storage_client = storage.Client()
bucket = storage_client.bucket('dimsim')
image_paths = []
for blob in list(bucket.list_blobs()):
image_paths.append("gs://dimsim/"+blob.name)
# We can send a maximum of 16 images per request.
start = 0
end = 16
label_output = []
for i in range(int(np.floor(len(image_paths)/16))+1):
requests = []
client = vision_v1.ImageAnnotatorClient()
for image_path in image_paths[start:end]:
image = types.Image()
image.source.image_uri = image_path
requests.append({
"image": image,
"features":
[{"type_": vision_v1.Feature.Type.LABEL_DETECTION}]
})
response = client.batch_annotate_images(requests=requests)
print("Waiting for operation to complete...")
for image_path, i in zip(image_paths[start:end], response.responses):
labels = [{label.description: label.score} for label in i.label_annotations]
labels = {k: v for d in labels for k, v in d.items()}
filename = os.path.basename(image_path)
l = {'filename': filename, 'labels': labels}
label_output.append(l)
start = start+16
end = end+16
print("almost there...")
#export results to JSON file
with open('image_results.json', 'w') as outputjson:
json.dump(label_output, outputjson, ensure_ascii=False)
