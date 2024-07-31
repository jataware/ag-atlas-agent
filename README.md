# Ag Atlas Agent

An agent for exploring the Africa Agriculture Adaptation Atlas.

```
export OPENAI_API_KEY=your key here
docker-compose up -d
```

This will kickoff a Docker build. Your notebook will be available at `localhost:8888`. Make sure to select the `ag_atlas` context (top left).

If you change the code and need to restart it:
```
docker-compose down
docker-compose build
docker-compose up
```