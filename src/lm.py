# dependencies for lm fhe
import matplotlib.pyplot as plt
import torch
from llm.load_huggingface import get_gpt2_model, get_gpt2_tokenizer
from llm.qgpt2_models import MultiHeadsQGPT2Model, SingleHeadQGPT2Model

# dependencies for pir
from pir.fast_pir import PIR
from pir.lhe import LHE
from sage.all import *

# hyperparams
q = 11
m = n = 2
N = 4
sqrtN = 2

# set up lhe and pir
lhe = LHE(q, m, n)
pir = PIR(lhe)

# potentially untrust db (hardcoded for now)
D = [[1, 0], [0, 1]]

def query_with_pir(i, j):
    qu, st = (pir.query(i, j, sqrtN))
    return (pir.reconstruct(pir.answer(matrix(GF(2), 2, 2, D), qu), st))[0]

gpt2_model = get_gpt2_model("gpt2_model")
gpt2_tokenizer = get_gpt2_tokenizer("gpt2_tokenizer")

input_sentence = f"cancer [{query_with_pir(1, 0)}] is not"

input_token_indexes = gpt2_tokenizer.encode(input_sentence)
input_ids = torch.tensor(input_token_indexes).unsqueeze(0)

output_ids = gpt2_model.generate(input_ids, max_new_tokens=4, use_cache=False)
print(gpt2_tokenizer.decode(output_ids[0]))
