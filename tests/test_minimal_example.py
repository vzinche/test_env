import torch

if torch.cuda.is_available():
    print("GPU is available")
    device = torch.device("cuda")


a = torch.ones(5)
a.to(device)

