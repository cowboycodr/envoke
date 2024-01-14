# Conjure

Conjure is a Python package that allows users to create and run keyboard macros with optional delays and randomness. It's designed to be simple yet flexible, providing a straightforward API for automating key presses.

## Installation

To install Conjure, run the following command:

```bash
pip install conjure
```

## Quick Start

Here's a simple example to get you started:

```python
from conjure import conjure

# Create a macro sequence
c = conjure(start_delay=2)
c.enter(interval=0.5).key('a', interval=0.1)

# Run the macro
c.run()
```

## Advanced Usage

Conjure also supports more advanced features, including continuous macros and random interval differences. See the `/examples` directory for more use cases.

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

Contributions to Conjure are welcome! I don't currently have a `CONTRIBUTING.md` so just submit them freely.

## License

Conjure is released under the [MIT License](LICENSE).