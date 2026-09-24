import torch
import torch.nn as nn
import torch.nn.functional as F

# The GPT model is provided for you. It returns raw logits (not probabilities).
# You only need to implement the training loop below.

class Solution:
    def train(self, model: nn.Module, data: torch.Tensor, epochs: int, context_length: int, batch_size: int, lr: float) -> float:
        # Train the GPT model using AdamW and cross_entropy loss.
        # For each epoch: seed with torch.manual_seed(epoch),
        # sample batches from data, run forward/backward, update weights.
        # Return the final loss rounded to 4 decimals.
        pass
        optimizer=torch.optim.AdamW(model.parameters(),lr=lr)
        model.train()
        for epoch in range(epochs):
            torch.manual_seed(epoch)
            maxstart=data.size(0)-context_length-1
            starts=torch.randint(0,maxstart+1,(batch_size,))
            x=torch.stack([
                data[i:i+context_length]
                for i in starts
            ])
            y=torch.stack([
                data[i+1:i+context_length+1]
                for i in starts
            ])
            logits=model(x)
            loss=F.cross_entropy(
                logits.reshape(-1,logits.size(-1)),
                y.reshape(-1)
            )
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
        return round(loss.item(),4)


