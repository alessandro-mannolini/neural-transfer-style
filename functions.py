
import torch
# pip list --format=freeze > requirements.txt

# Funzione per normalizzare un tensore
def normalize(tensor):
    mean = torch.tensor([0.485, 0.456, 0.406]).view(-1, 1, 1)
    std = torch.tensor([0.229, 0.224, 0.225]).view(-1, 1, 1)
    return (tensor - mean) / std

# Denormalizza l'immagine
def denormalize(tensor):
    mean = torch.tensor([0.485, 0.456, 0.406]).view(-1, 1, 1)
    std = torch.tensor([0.229, 0.224, 0.225]).view(-1, 1, 1)
    
    tensor = tensor * std + mean
    tensor = torch.clamp(tensor, 0, 1)  # I valori potrebbero essere leggermente fuori dal range [0,1] a causa di piccoli errori numerici, quindi li limitiamo.
    return tensor