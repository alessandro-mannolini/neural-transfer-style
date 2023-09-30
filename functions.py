
import torch
import torch.nn as nn
import torchvision.models as models

# modello semplice usato in precedenza
class VGG(nn.Module):
    def __init__(self):
        super(VGG, self).__init__()
        
        self.chosen_features = ["0", "5", "10", "19", "28"]
        self.model = models.vgg19(weights = models.VGG19_Weights.DEFAULT).features[:29]
        
    def forward(self, x):
        features = []
        
        for layer_num, layer in enumerate(self.model):
            x = layer(x)
            
            if str(layer_num) in self.chosen_features:
                features.append(x)
                
        return features
    


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