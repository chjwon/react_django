import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from lstm_utils import LSTMModel, hidden_size, output_size, num_layers
import json

with open("./file_path.json", 'r') as file:
    fileName = json.load(file)['prediction_csv'][0]

file_path = fileName['ms_stock_file']
df = pd.read_csv(file_path)

features = df[['Open', 'High', 'Low', 'Close', 'Volume']]

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_close = scaler.fit_transform(df[['Close']])

joblib.dump(scaler, 'close_scaler.pkl')
scaler = joblib.load('close_scaler.pkl')

# test_value = df['Close'].values[:5]
# normalized_value = scaler.transform(test_value.reshape(-1, 1))
# recovered_value = scaler.inverse_transform(normalized_value)

# print(f"Original Close Values: {test_value}")
# print(f"Normalized Close Values: {normalized_value}")
# print(f"Recovered Close Values: {recovered_value}")

def create_sequences(data, target, seq_length):
    xs, ys = [], []
    for i in range(len(data) - seq_length):
        x = data[i:i + seq_length]
        y = target[i + seq_length]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

sequence_length = 20
X, y = create_sequences(features.values, scaled_close, sequence_length)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, shuffle=False)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_val = torch.tensor(X_val, dtype=torch.float32)
y_val = torch.tensor(y_val, dtype=torch.float32)

input_size = X_train.shape[2]
learning_rate = 1e-4


model = LSTMModel(input_size, hidden_size, output_size, num_layers)

criterion = nn.MSELoss()  # Mean Squared Error for regression
optimizer = optim.Adam(model.parameters(), lr=learning_rate)


patience = 20
best_val_loss = float('inf')
counter = 0

epochs = 500
for epoch in range(epochs):
    model.train()
    output = model(X_train)
    loss = criterion(output.squeeze(), y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    model.eval()
    with torch.no_grad():
        val_output = model(X_val)
        val_loss = criterion(val_output.squeeze(), y_val)

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            counter = 0
            torch.save(model.state_dict(), 'lstm_stock_model.pth')
            print(f'New best model saved with validation loss: {val_loss.item():.4f}')
        else:
            counter += 1
            if counter >= patience:
                print(f'Early stopping at epoch {epoch+1}')
                break

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}, Validation Loss: {val_loss.item():.4f}')

model.load_state_dict(torch.load('lstm_stock_model.pth'))
model.eval()
with torch.no_grad():
    predicted = model(X_train)
    predicted_close = scaler.inverse_transform(predicted.squeeze().numpy().reshape(-1, 1))
    actual_close = scaler.inverse_transform(y_train.numpy().reshape(-1, 1))

print(f'Predicted Close: {predicted_close[:5]}')
print(f'Actual Close: {actual_close[:5]}')
