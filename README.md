# uv-demo

Minimal Python project managed with [uv](https://docs.astral.sh/uv/).

## 1. Install uv (once)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh                        # macOS / Linux
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"             # Windows
```

## 2. Use this project

```bash
uv sync              # creates .venv/ and installs everything from uv.lock
uv run uv-demo       # run the CLI entry point  -> "Invariant mass: 135.0 MeV"
uv run pytest        # run the tests
```

No manual `venv` / `activate` / `pip install` needed: `uv run` always uses the project's `.venv`.

## 3. Common commands

```bash
uv add scipy         # add a dependency (updates pyproject.toml + uv.lock)
uv add --dev ruff    # add a dev-only tool
uv remove scipy      # remove it again
uv run python        # Python shell inside the env
uv run --with jupyterlab jupyter lab   # Jupyter without adding it to the project
```

## 4. Start your own project from scratch

```bash
uv init --package myproject
cd myproject
uv add numpy
```

## Files

| File | Purpose |
|---|---|
| `pyproject.toml` | Project metadata + dependencies (edit by hand or via `uv add`) |
| `uv.lock` | Exact pinned versions — commit it, so everyone gets the same env |
| `.python-version` | Python version uv uses (downloaded automatically if missing) |
| `src/uv_demo/` | The package code |
| `tests/` | pytest tests |
