Code reviewer. Read the source.

How to setup?

```
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
ln -s /path/to/your/project/code_review.py /Users/krystofrehacek/.local/bin/code-review
```

and change the python interpreter in shebang to the current python.

```
SUPERPC:Repos/code-review ‹master*›$ which python3
/Users/krystofrehacek/Repos/code-review/.venv/bin/python3
```
