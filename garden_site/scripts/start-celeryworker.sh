#!/bin/bash

set -o errexit
set -o nounset

celery -A weathersensor worker -l INFO