import torch
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

def main():
    # Define the dataset
    data = [['X','X','X','X','O','O','X','O','O'],
            ['O','O','X','X','X','O','O','X','X'],
            ['O','X','O','O','X','X','X','O','X'],
            ['X','X','X','X','O','O','O','X','O']]
    
    labels = [1, 0, 0, 1]  

    dataset = CustomDataset(data, labels)

    print(f"Dataset Length: {len(dataset)}")
    print(f"Second Sample: {dataset[1]}")

    # Use DataLoader to handle batching, shuffling, etc.
    dataloader = DataLoader(dataset, batch_size=2, shuffle=True)
    
    # Iterate through the DataLoader
    for batch_data, batch_labels in dataloader:
        print(f"Batch Data: {batch_data}")
        print(f"Batch Labels: {batch_labels}")

if __name__ == "__main__":
    main()
