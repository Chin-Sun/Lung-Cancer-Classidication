import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torchvision import models
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

# Assuming the same directory structure and preprocessing functions
train_path_str = 'C:/Master/COEN6313/Project/code/dataset/Data/train'
val_path_str = 'C:/Master/COEN6313/Project/code/dataset/Data/valid'
test_path_str = 'C:/Master/COEN6313/Project/code/dataset/Data/test'

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

num_classes = 4

train_data = torchvision.datasets.ImageFolder(root=train_path_str, transform=transform)
val_data = torchvision.datasets.ImageFolder(root=val_path_str, transform=transform)
test_data = torchvision.datasets.ImageFolder(root=test_path_str, transform=transform)

train_loader = torch.utils.data.DataLoader(train_data, batch_size=16, shuffle=True)
val_loader = torch.utils.data.DataLoader(val_data, batch_size=16, shuffle=False)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=16, shuffle=False)

# Initialize pre-trained ResNet model
resnet = models.resnet18(pretrained=True)
# Modify the fully connected layer to fit the number of classes
num_ftrs = resnet.fc.in_features
resnet.fc = nn.Sequential(
    nn.Linear(num_ftrs, 1024),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(1024, 512),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(512, 256),
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, num_classes)
)

# Set model to device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
resnet.to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(resnet.parameters(), lr=0.001)

# Training loop
num_epochs = 100
for epoch in range(num_epochs):
    resnet.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = resnet(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    resnet.eval()
    # Validation loop (optional)
    with torch.no_grad():
        # Perform validation here if needed
        pass

# Save the trained model
torch.save(resnet.state_dict(), 'C:\Master\COEN6313\Project\pytorch_model\saved')

# Testing the model
resnet.eval()
all_preds = []
true_labels = []
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = resnet(images)
        _, predicted = torch.max(outputs, 1)
        all_preds.extend(predicted.cpu().numpy())
        true_labels.extend(labels.cpu().numpy())

# Calculate metrics
print(classification_report(true_labels, all_preds))
conf_mat = confusion_matrix(true_labels, all_preds)
print(conf_mat)
