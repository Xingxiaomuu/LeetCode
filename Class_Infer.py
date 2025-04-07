import torch
from Class_Train import CharRNN, char_to_idx, idx_to_char

def generate_text(model, start_str, length=100, temperature=1.0):
    model.eval()
    chars = [ch.lower() for ch in start_str]
    hidden = model.init_hidden(1)
    
    for ch in chars[:-1]:
        x = torch.tensor([[char_to_idx[ch]]])
        _, hidden = model(x, hidden)
    
    input_char = chars[-1]
    for _ in range(length):
        x = torch.tensor([[char_to_idx[input_char]]])
        output, hidden = model(x, hidden)
        
        probs = torch.softmax(output[0,-1] / temperature, dim=0)
        pred_idx = torch.multinomial(probs, 1).item()
        pred_char = idx_to_char[pred_idx]
        
        chars.append(pred_char)
        input_char = pred_char
    
    return ''.join(chars)

if __name__ == "__main__":
    model = CharRNN()
    model.load_state_dict(torch.load('char_rnn.pth'))
    print(generate_text(model, "The melting moon", length=600))
    
