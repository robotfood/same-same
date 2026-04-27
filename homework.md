# spaCy and en-core-web-md

## What spaCy is

spaCy is a Python library for natural language processing. It turns text into structured objects that software can inspect, compare, and transform.

In this project, spaCy is used to convert defect descriptions into numeric vectors. Those vectors let the app compare text by meaning instead of only checking whether the exact same words appear.

For example, these two descriptions may not share many exact words:

```text
Login page crashes after password reset
Password reset causes sign-in screen failure
```

A semantic model can still place them near each other because the meaning is similar.

## What en-core-web-md is

`en-core-web-md` is a pretrained English model for spaCy. The name breaks down like this:

- `en`: English
- `core`: general-purpose NLP pipeline
- `web`: trained from web text
- `md`: medium-sized model

The important part for this app is that `en-core-web-md` includes word vectors. Word vectors are arrays of numbers that represent meaning. spaCy combines word vectors into a vector for a whole document or sentence.

The code loads it here:

```python
spacy.load("en_core_web_md")
```

Then each defect description gets converted into a 300-number vector. The matcher can compare those vectors with cosine similarity to find likely duplicate defects.

## Why this project depends on it

The `same-same` tool needs semantic matching. A smaller spaCy model such as `en_core_web_sm` is useful for tokenization and tagging, but it does not provide the same pretrained word vectors. Without those vectors, the duplicate detection would be much weaker.

By adding `en-core-web-md` to `pyproject.toml`, `uv sync` can install the model automatically. That makes the project easier to set up and makes tests more reproducible in a fresh environment.

## How uv fits in

`uv` reads `pyproject.toml`, resolves the dependencies, and records the exact result in `uv.lock`.

For this project:

```bash
uv sync --group dev
uv run pytest
uv run same-same --config mock_config.json
```

`uv sync --group dev` installs the app, runtime dependencies, dev tools like `pytest`, and the `en-core-web-md` model.
