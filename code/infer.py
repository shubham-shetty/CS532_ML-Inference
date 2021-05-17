import io, json
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

# Pre-load transformations and model
model = models.densenet121(pretrained=True)
model.eval()
imagenet_class_index = json.load(open('../data/imagenet_class_index.json'))
densenet_transform = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])

def get_prediction(image_bytes):
    # Transform image based on pre-trained requirements
    image = Image.open(io.BytesIO(image_bytes))
    tensor = densenet_transform(image).unsqueeze(0)
    # Execute the model
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    # Map prediction to output label
    return imagenet_class_index[predicted_idx]
