# Xpyron

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Documentation Status](https://readthedocs.org/projects/xpyron/badge/?version=latest)](https://xpyron.readthedocs.io/en/latest/?badge=latest)

</div>

A comprehensive educational deep learning framework designed to illuminate neural network concepts through intuitive implementations and visual demonstrations. Xpyron combines rigorous mathematical foundations with clear visual representations, making complex deep learning concepts accessible to students, researchers, and practitioners.

## 🚀 Features

- **Step-by-Step Network Construction**: Build neural networks from scratch while understanding each component
- **Interactive Visualizations**: Gain insights through dynamic visual representations of network architectures and learning processes
- **Educational Focus**: Clear implementations prioritizing understanding over optimization
- **Comprehensive Tutorials**: From basic perceptrons to advanced architectures
- **Mathematical Foundations**: Strong emphasis on the underlying mathematical concepts
- **Visual Learning**: Rich visualizations to reinforce theoretical concepts

## 📦 Installation

```bash
pip install xpyron
```

Requirements:
- Python 3.12+
- NumPy ≥ 1.24.0
- Matplotlib ≥ 3.7.0
- scikit-learn ≥ 1.2.0

## 🎓 Quick Start

```python
from xpyron import NeuralNetwork
from xpyron.visualize import plot_network

# Create a simple neural network
model = NeuralNetwork([
    ('input', 784),
    ('dense', 128, 'relu'),
    ('dense', 10, 'softmax')
])

# Train the model
model.fit(X_train, y_train, epochs=10)

# Visualize the network architecture
plot_network(model)

# Make predictions
predictions = model.predict(X_test)
```

## 📚 Documentation

For detailed documentation, tutorials, and examples, visit our [documentation page](https://xpyron.readthedocs.io).

### Examples

- [Basic Perceptron](https://xpyron.readthedocs.io/en/latest/examples/perceptron.html)
- [Feedforward Neural Networks](https://xpyron.readthedocs.io/en/latest/examples/feedforward.html)
- [Convolutional Neural Networks](https://xpyron.readthedocs.io/en/latest/examples/cnn.html)
- [Recurrent Neural Networks](https://xpyron.readthedocs.io/en/latest/examples/rnn.html)

## 🤝 Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details on how to help improve Xpyron.

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes
4. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Dr. Saad L. ([@dr-saad-la](https://github.com/dr-saad-la))

## 📣 Citation

If you use Xpyron in your research, please cite:

```bibtex
@software{xpyron2025,
  author = {L., Saad},
  title = {Xpyron: An Educational Deep Learning Framework},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/dr-saad-la/xpyron}
}
```

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=dr-saad-la/xpyron&type=Date)](https://star-history.com/#dr-saad-la/xpyron&Date)
