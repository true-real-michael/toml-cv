# Boy do I hate LaTeX
## So here is a TOML-based CV with HTML rendering

### Usage
Prerequisites: [uv](https://github.com/astral-sh/uv).

1. Clone and install the dependencies:
```shell
git clone https://github.com/true-real-michael/toml-cv.git
cd toml-cv
uv sync
cp cv.example.toml cv.toml
```
2. Edit the `cv.toml`
3. Run the converter script:
```shell
uv run cv.py
```

🎉 Done. Your CV is in the `cv-out.html` file. Open it in your favourite browser and save as PDF. 