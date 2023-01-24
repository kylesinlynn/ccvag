# 💳 CCVAG
> This python package is inspired by [Luhn](https://github.com/amm834/luhn) and [Panify](https://github.com/amm834/panify).

`CCVAG` stands for Credit Card Validator and Generator.

# Content
- [💳 CCVAG](#-ccvag)
- [Content](#content)
- [Installation](#installation)
- [Uses](#uses)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

# Installation
```bash
python -m pip install ccvag
```

# Uses
After [Installation](#installation) process, you can import `validator` or `generator` from `ccvag`.

```python
from ccvag import validator, generator

# Validate the credit card
print(validator('4242424242424242'))

# Generate the credit cards
# First Arg - must be the first-sixth number which you might choose to enter by yourself
# Second Arg - would be the count which the function will generate
print(generator('424242', 50))

```

# Troubleshooting
Create an issue upon your error that is associated with this project.

# Contributing
Feel free to fork and create pull requests. Your contribution will be appreciated.

# License
This project is licensed under [BSD License](LICENSE).