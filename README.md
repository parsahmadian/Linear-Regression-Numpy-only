# Linear Regression from Scratch (Python & NumPy)

This project is a **from-scratch implementation of multivariate linear regression**
using only **Python and NumPy**, without any machine learning libraries.

## 🎯 Goal
To deeply understand:
- How linear regression works internally
- How loss functions affect learning
- How gradient descent updates model parameters
- The impact of learning rate and feature scale on training stability

## 🧠 Model
The model predicts output using:
```
ŷ = X · w + b
```

Where:
- X: input features
- w: weights
- b: bias

Loss function:
- Mean Squared Error (MSE)

Optimization:
- Gradient Descent

## 📊 Results
- Training loss decreases steadily
- Demonstrates convergence behavior
- Shows instability when learning rate is too large (overflow / NaN)

## ⚠️ Notes
- In previous versions, No feature standardization was applied intentionally to observe its effect
- Learning rate was carefully tuned to avoid divergence

## 🛠 Tech Stack
- Python
- NumPy
- Pandas
- Matplotlib

## 🚀 Why this project?
This project focuses on **conceptual understanding**, not just usage of libraries.
It demonstrates my ability to:
- Implement ML algorithms from scratch
- Debug numerical instability
- Reason about optimization behavior
