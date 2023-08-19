# Budgeter - Elegant Expenses

For a deep dive, check out my [blog post](https://blog.tanishq.page/posts/homelab-budgeter/) for deploying and using this app in a home lab.

This application can be used to &rarr;

- expose an API to record expenses
- expose a simple text-based website to showcase the recorded expenses
- store expenses as JSON files corresponding to each month
- make a collated CSV for all expenses for further processing and visualization

Assuming that the application is deployed at a system with the hostname `galaxy`, visit `http://galaxy.local` for using the app.

For running the docker image, do the following &rarr;

```bash
mkdir expense-data
docker run -v $PWD/expense-data/:/expense-data --name budgeter --rm -p 80:5000 -d -t tanq16/budgeter:main
# use tage :main_arm for ARM64 image (useful for apple silicon and raspberry pi)
```

This will launch the container as a daemon and it'll be reachable at port 80 on the host machine.

---
