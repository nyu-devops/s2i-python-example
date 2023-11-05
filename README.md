# S2I Python Example

This repo contains a very basic Python Flask application to be used with OpenShift S2I to show how easy it is to deploy a Python app to OpenShift without having to know anything about Docker or Kubernetes.

## OpenSHift Sandbox

You can get an OpenShift Sandbox cluster to deploy this repo in by going to [developers.redhat.com](http://developers.redhat.com) and registering for a free Red Hat account, after which you will be able to request a free OpenShift Sandbox.

## The Magic

There is no `Dockerfile`. As the name implies, source-2-image will take your source code and match it with a builder image so that you don't have to know anything about Docker.

There are no Kubernetes manifests! (Look Ma' no `YAML`!) Source to image will also deploy your application to kubernetes for you in OpenShift.

## What's featured in the project?

This project is just a very basic `app.py` that has the following endpoints:

- `/` - The home page
- `/health` - The health endpoint
- `/hello` - Returns "Hello World"

```text
./app.py -- the main Service using Python Flask
```

## License

Copyright (c) 2023, John J. Rofrano. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)

This repository is part of the NYU graduate class **CSCI-GA.2810-001: DevOps and Agile Methodologies** taught by [John Rofrano](http://cs.nyu.edu/~rofrano/), Adjunct Instructor, NYU Courant Institute, Graduate Division, Computer Science.
