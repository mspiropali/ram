# Venv
### activate
```bash
source .venv/bin/activate
```

### deactivate
```bash
deactivate
```


# Run FastAPI Server

```bash
uv run uvicorn main:app --reload
```
### Optional arguments

> * `--host <0.0.0.0>    to run at specific ip`
> * `--port <5000>       to run at specific port`
> * `--workers <4>       specify number of threads`
> * `--log-level <info>  to set the desired log level`

