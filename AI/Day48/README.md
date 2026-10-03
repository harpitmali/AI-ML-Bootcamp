# Day 48 — Transformer Fundamentals

## Overview

This day covers the foundational concepts behind Transformer architectures
and self-attention.

## Topics Covered

- Why Transformers?
- Tokenization
- Token IDs
- Token Embeddings
- Positional Information
- Sinusoidal Positional Encoding
- Attention Intuition
- Query, Key, Value
- Scaled Dot-Product Attention
- Self-Attention
- Causal Attention
- Attention masking
- Attention matrix shapes

## Implementations

- Tokenization experiments
- Token embedding lookup
- Positional encoding with NumPy
- Simplified self-attention
- Causal self-attention

## Main Formula

Attention(Q,K,V)
=
softmax(QK^T / sqrt(d_k))V

## Goal

Understand how the core self-attention mechanism works before moving
toward modern Transformer and LLM architectures.