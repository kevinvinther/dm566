import torch
from torch.autograd import Variable
import torchvision.transforms as transforms
import torchvision.datasets as dsets
import matplotlib.pyplot as plt

# Step 1. Load Dataset
# transforms.ToTensor() does the following:
# It converts the images into numbers, that are understandable by the system. 
# It separates the image into three color channels (separate images): red, green & blue. 
# Then it converts the pixels of each image to the brightness of their color between 0 and 255. 
# These values are then scaled down to a range between 0 and 1. The image is now a Torch Tensor.
train_dataset = dsets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = dsets.MNIST(root='./data', train=False, transform=transforms.ToTensor(), download=True)
print(train_dataset) # We see that there are 60k training datapoints
print(test_dataset) # We see that there are 10k test datapoints

# We use matplotlib to visualize some samples in our training data.
labels_map = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
}
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(train_dataset), size=(1,)).item()
    img, label = train_dataset[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()

# Step 2. Set our parameters
batch_size = 100
epochs = 15
# input_dim is 784 since we flatten out each image before sending it inside the neural network. (28 x 28 = 784)
input_size = 784
output_size = 10
lr_rate = 0.01

# Step 3. Make Dataset Iterable
# We prepare the data for training with DataLoaders.
# While training a model, we typically want to pass samples in “minibatches”, 
# reshuffle the data at every epoch to reduce model overfitting, 
# and use Python’s multiprocessing to speed up data retrieval.
# DataLoader is an iterable that abstracts this complexity for us in an easy API.
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)

# Step 4. Create Model
# nn.Linear applies a linear transformation to the incoming data.
model = torch.nn.Linear(input_size, output_size)
print(model)

# Step 5. Instantiate Loss Class
# The word ‘loss’ means the penalty that the model gets for failing to yield the desired results.
# This function will determine your model’s performance by comparing its predicted output
# with the expected output. If the deviation between y_pred and y is very large, 
# the loss value will be very high. If the deviation is small or the values are nearly identical,
# it’ll output a very low loss value. Therefore, you need to use a loss function that can 
# penalize a model properly when it is training on the provided dataset.
# Cross Entropy loss is used in classification problems, so we use this one.
criterion = torch.nn.CrossEntropyLoss()

# Step 6. Instantiate Optimizer Class
# We make use of torch.optim which is a module provided by PyTorch
# to optimize the model, perform gradient descent and update the weights by back-propagation. 
# Thus in each epoch (number of times we iterate over the training set), 
# we will be seeing a gradual decrease in training loss.
optimizer = torch.optim.SGD(model.parameters(), lr=lr_rate)

# Step 7. Train Model
for e in range(epochs):
    running_loss = 0
    for images, labels in train_loader:
        # Flatten MNIST images into a 784 long vector
        images = images.view(images.shape[0], -1)
    
        # Training pass
        optimizer.zero_grad()
        
        output = model(images)
        loss = criterion(output, labels)
        
        # This is where the model learns by backpropagating
        loss.backward()
        
        # And optimizes its weights here
        optimizer.step()
        
        running_loss += loss.item()
    else:
        print("Epoch {} - Training loss: {}".format(e, running_loss/len(train_loader)))

correct_count, all_count = 0, 0
for images,labels in test_loader:
  for i in range(len(labels)):
    img = images[i].view(1, 784)
    with torch.no_grad():
        logps = model(img)

    
    ps = torch.exp(logps)
    probab = list(ps.numpy()[0])
    pred_label = probab.index(max(probab))
    true_label = labels.numpy()[i]
    if(true_label == pred_label):
      correct_count += 1
    all_count += 1

print("Number Of Images Tested =", all_count)
print("\nModel Accuracy =", (correct_count/all_count))