#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/../AirBnB_clone"
{
    # This file lists all individuals having
    # contributed content to the repository
    echo
    git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
