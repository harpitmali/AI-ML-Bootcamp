# Day 48 — Transformers Fundamentals

## 1. Why Transformers?

Transformers use attention to model relationships between tokens.

Compared with RNNs/LSTMs:
- tokens can directly interact through self-attention
- processing can be much more parallelizable
- long-range relationships can be modeled more directly

---

## 2. Tokenization

Text is converted into tokens.

Example:

"I love AI"

-> tokens
-> token IDs

Important:
- tokens are not necessarily complete words
- subword tokenization is common
- token ID is only an identifier
- token count affects context usage, latency, and cost

Pipeline:

Text
-> Tokenizer
-> Token IDs

---

## 3. Token Embeddings

Token IDs are mapped to learned vectors.

Embedding matrix:

(vocabulary_size, embedding_dimension)

Token ID selects a row from the embedding matrix.

Token ID:
- identifier only
- no inherent semantic meaning

Embedding:
- learned numerical representation

---

## 4. Positional Information

Attention alone does not inherently provide token order.

Example:

"The dog chased the cat"

and

"The cat chased the dog"

need different interpretation.

Transformer input:

X = E + P

E = token embedding
P = positional information

Original Transformers used sinusoidal positional encoding.

Modern Transformer architectures may use other positional methods such as RoPE.

---

## 5. Attention Intuition

Attention allows each token to determine which other tokens are relevant.

Q = What am I looking for?
K = What information do I contain?
V = What information can I provide?

Conceptually:

Query
-> compare with Keys
-> attention scores
-> softmax
-> attention weights
-> weighted Values
-> contextual representation

---

## 6. Self-Attention

It is called self-attention because Q, K, and V are derived from the same input sequence.

Projection:

Q = XW_Q
K = XW_K
V = XW_V

Attention:

Attention(Q,K,V)
=
softmax(QK^T / sqrt(d_k)) V

Steps:

1. Create Q, K, V
2. Calculate QK^T
3. Scale by sqrt(d_k)
4. Apply softmax
5. Use weights to combine V

---

## 7. Attention Shapes

If:

X = (sequence_length, d_model)

W_Q = (d_model, d_k)
W_K = (d_model, d_k)
W_V = (d_model, d_v)

Then:

Q = (sequence_length, d_k)
K = (sequence_length, d_k)
V = (sequence_length, d_v)

QK^T:

(sequence_length, sequence_length)

Final output:

(sequence_length, d_v)

---

## 8. Causal Attention

Causal attention prevents a token from attending to future tokens.

For 4 tokens:

[1 0 0 0]
[1 1 0 0]
[1 1 1 0]
[1 1 1 1]

Future positions are masked before softmax.

This is important for autoregressive language generation.

---

## 9. Attention Implementation

Basic implementation:

Q = X @ W_Q
K = X @ W_K
V = X @ W_V

scores = Q @ K.T

scaled_scores = scores / sqrt(d_k)

attention_weights = softmax(scaled_scores)

output = attention_weights @ V

For causal attention, apply the causal mask before softmax.

---

## 10. Key Mental Model

Tokenization
-> What pieces of text do we have?

Embeddings
-> What numerical representation do those tokens have?

Position
-> Where are the tokens?

Attention
-> Which tokens are relevant to each other?

Values
-> What information should be combined?

Output
-> Contextual representation of each token