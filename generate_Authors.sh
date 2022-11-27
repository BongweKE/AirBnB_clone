#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/../AirBnB_clone"

# see also ".mailmap" for how email addresses and names are deduplicated

{

    # This file lists all individuals having
    # contributed content to the repository

	echo
        git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
