
import torch.nn as nn
import torch

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, dropout=0.3)

        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        h0 = torch.zeros(num_layers, x.size(0), hidden_size).to(x.device)  # Hidden state
        c0 = torch.zeros(num_layers, x.size(0), hidden_size).to(x.device)  # Cell state
        
        out, _ = self.lstm(x, (h0, c0))  # LSTM forward pass
        out = self.fc(out[:, -1, :])  # Output of the last time step
        return out


hidden_size = 50
output_size = 1
num_layers = 1