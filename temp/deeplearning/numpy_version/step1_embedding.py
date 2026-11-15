import numpy as np

text = "hello transformer"
chars = sorted(set(text))
vocab_size = len(chars)

stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}

print(f"stoi: {stoi}")
print(f"itos: {itos}")

def encode(s): return [stoi[c] for c in s]
def decode(ids): return "".join(itos[i] for i in ids)

d_model = 8
rng = np.random.default_rng(0)
E = rng.normal(0, 1, (vocab_size, d_model))

ids = np.array(encode("hello")) # 정수 번호
x = E[ids]

print(ids)
print(x)
