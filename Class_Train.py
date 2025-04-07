import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# 定义全局变量
text = """The golden sun rises over the horizon, painting the sky with hues of pink and orange. Gentle waves lap against the shore, their rhythmic whispers blending with the distant calls of seagulls. A soft breeze rustles through the towering pine trees, carrying the crisp scent of morning dew and wildflowers. Rolling hills stretch into the distance, their emerald slopes bathed in the warm glow of daylight. A crystal-clear river winds through the valley, its waters shimmering like liquid silver under the sun's embrace. In the heart of the forest, a hidden waterfall cascades down moss-covered rocks, its soothing murmur harmonizing with the chirping of birds. The world awakens in perfect harmony, a testament to nature’s timeless beauty."""

chars = sorted(list(set(text.lower())))
char_to_idx = {ch: i for i, ch in enumerate(chars)}
idx_to_char = {i: ch for i, ch in enumerate(chars)}
vocab_size = len(chars)

seq_length = 50
batch_size = 32
hidden_size = 256
num_layers = 2
num_epochs = 50
learning_rate = 0.001

data = [char_to_idx[ch.lower()] for ch in text]

class TextDataset(Dataset):
    def __init__(self, data, seq_length):
        self.data = data
        self.seq_length = seq_length

    def __len__(self):
        return len(self.data) - self.seq_length

    def __getitem__(self, idx):
        inputs = self.data[idx : idx+self.seq_length]
        target = self.data[idx+1 : idx+self.seq_length+1]
        return torch.tensor(inputs), torch.tensor(target)

dataset = TextDataset(data, seq_length)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

class CharRNN(nn.Module):
    def __init__(self):
        super(CharRNN, self).__init__()
        self.embed = nn.Embedding(vocab_size, hidden_size)
        self.rnn = nn.GRU(hidden_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x, hidden):
        x = self.embed(x)
        out, hidden = self.rnn(x, hidden)
        out = self.fc(out)
        return out, hidden

    def init_hidden(self, batch_size):
        return torch.zeros(num_layers, batch_size, hidden_size)

def train():
    model = CharRNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        #hidden = model.init_hidden(batch_size)
        total_loss = 0
        
        for inputs, targets in dataloader:
            optimizer.zero_grad()
            batch_size = inputs.shape[0]  # 这里获取 batch_size
            hidden = model.init_hidden(batch_size).to(inputs.device).detach()  # 在循环内初始化
            
            outputs, hidden = model(inputs, hidden)
            loss = criterion(outputs.transpose(1, 2), targets)
            
            loss.backward()
            # **打印梯度信息**
            print("Gradients:")
            for name, param in model.named_parameters():
                if param.grad is not None:
                    print(f"{name}: {param.grad.norm().item():.6f}", flush=True)  # 仅打印梯度的范数，防止输出过多数据
                else:
                    print(f"{name}: No gradient")
            optimizer.step()
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(dataloader)
        print(f'Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}')

    torch.save(model.state_dict(), 'char_rnn.pth')

if __name__ == "__main__":
    train()

'''

'''