# Architecture Performance Analysis using gem5

## 📌 Overview
This project analyzes key performance aspects of computer architecture using the gem5 simulator.

It focuses on two major areas:
1. Cache Replacement Policies (LRU, FIFO, Random)
2. Control Hazards and Branch Prediction

## 🎯 Objectives
- To compare cache replacement techniques and their impact on performance
- To study control hazards and branch misprediction effects
- To evaluate performance differences between CPU models

## ⚙️ CPU Models Used
- TimingSimpleCPU
- O3 CPU

## 🧪 Experiments Conducted

### 1. Cache Replacement Policies
- LRU (Least Recently Used)
- FIFO (First In First Out)
- Random Replacement

Metrics:
- Cache hits/misses
- Execution time

### 2. Control Hazard Analysis
- Branch behavior analysis
- Pipeline performance comparison

Metrics:
- CPI (Cycles per Instruction)
- Branch misprediction rate
- Number of cycles

## 📁 Project Structure
The project is organized into separate folders for each experiment:

- Cache Replacement → Policy → CPU → Results
- Control Hazard → Technique → CPU → Results

## 📊 Results
Includes:
- stats.txt files from gem5
- Execution logs
- Performance comparison graphs

## 🛠 Tools Used
- gem5 simulator
- Python
- Linux

## 👨‍💻 Author
Arjun Sagar
