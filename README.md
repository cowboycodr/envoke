# Envoke

<a href="https://pepy.tech/project/envoke"><img src="https://img.shields.io/pypi/dw/envoke"></a>
<a href="https://pypi.org/project/envoke"><img src="https://img.shields.io/pypi/v/envoke"></a>
<a href="https://github.com/cowboycodr/envoke"><img src="https://img.shields.io/github/repo-size/cowboycodr/envoke"></a>

Envoke is a Python package that allows users to create and run keyboard macros with optional delays and randomness. It's designed to be simple yet flexible, providing a straightforward API for automating key presses.

## Installation

To install Envoke, run the following command:

```bash
pip install envoke
```

## Quick Start

Here's a simple example to get you started:

```python
from envoke import envoke

# Create a macro sequence
e = envoke()
e.enter(interval=0.5).key('a', interval=0.1)

# Run the macro
e.run(start_delay=3)
```

## Advanced Usage

Envoke also supports more advanced features, including continuous macros and random interval differences. See the `/examples` directory for more use cases.

## Examples

### Basic Usage

```python
# See examples/basic_usage.py
```

### Advanced Features

```python
# See examples/advanced_features.py
```

### Using Number Keys

```python
# See examples/number_keys_example.py
```

## Documentation

Will work on this eventually. For right now `/examples` should suffice.

## Contributing

Contributions to Envoke are welcome! I don't currently have a `CONTRIBUTING.md` so just submit them freely.

## Packaging

To package Envoke for distribution, follow these steps:

```bash
# Ensure you are in the root directory of the project
python -m build
```

After the build is successful, you can upload the package to PyPI using twine:

```bash
python -m twine upload dist/*
```

## License

Envoke is released under the [MIT License](LICENSE).