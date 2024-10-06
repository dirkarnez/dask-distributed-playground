dask-distributed-playground
===========================
### Tutorials
- [Quickstart — Dask.distributed 2024.9.0 documentation](https://distributed.dask.org/en/stable/quickstart.html)
- 

### Notes
- start master by run `master\start.cmd` first, then copy master's LAN IP to worker `worker\start.cmd` and run it. Finally modify client's code `client\main.py` for custom logic and run `client\start.cmd` to get result from distributed computing
- There should be single master. We can run multiple workers on same / different machines.

### Endpoints
- `http://<IP of master node>:8787/status` for dashboard
