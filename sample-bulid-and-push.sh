#!/bin/bash

# ------------ Get the version ------------
printf "Enter version number: "
read VERSION

# ------------ Remove the image if already exists ------------
docker image rm ghcr.io/<organization-name>/<package-name>:"$VERSION"

# ------------ build the image ------------
docker buildx build -t ghcr.io/<organization-name>/<package-name>:"$VERSION" .

# ------------ push the image ------------
docker push ghcr.io/<organization-name>/<package-name>:"$VERSION"
