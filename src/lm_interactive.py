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

while True:
    input_sentence = input("Enter your prompt: ")
    index_i = input("Enter the i-coordinate of the bit to query (0 or 1) ")
    index_j = input("Enter the j-coordinate of the bit to query (0 or 1) ")

    try:
        index_i = int(index_i)
        index_j = int(index_j)
        assert index_i == 0 or index_i == 1
        assert index_j == 0 or index_j == 1
    except:
        raise ValueError("invalid input indices")

    input_token_indexes = gpt2_tokenizer.encode(f"[{query_with_pir(index_i, index_j)}] {input_sentence} ")
    input_ids = torch.tensor(input_token_indexes).unsqueeze(0)

    output_ids = gpt2_model.generate(input_ids, max_new_tokens=20, use_cache=False)
    print(gpt2_tokenizer.decode(output_ids[0]))
