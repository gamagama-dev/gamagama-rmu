# gamagama-rmu

`gamagama-rmu` (Game Master Game Manager — Role Master Unified) is a game system plugin for `gamagama-cli` implementing the [Rolemaster Unified](https://www.ironcrown.com/) (RMU) rule system.

It provides `RMUSystem`, a `GameSystem` subclass, and `RMUDiceEngine`, which implements open-ended percentile dice rolls as specified by the RMU rules.

## Installation

`gamagama-rmu` is a plugin. Install it into the same environment as `gamagama-cli`:

```bash
pip install .
```

Once installed, `gamagama-cli` discovers it automatically via the `gamagama.systems` entry point and makes `rmu` available as a selectable game system.

## Dice Mechanics

The RMU engine handles the open-ended percentile roll (`d%!`):

| First roll | Behaviour |
|------------|-----------|
| 96–100 | Roll again and **add** (repeats while result is 96–100) |
| 06–95 | Use as-is |
| 01–05 | Roll again and **subtract** (repeats while result is 96–100) |

For all other die types, standard rolling rules apply.

## Contributing

To run the tests:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
pytest
```
