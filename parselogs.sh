#!/bin/bash
curl -s https://coderbyte.com/api/challenges/logs/web-logs-raw -O > /dev/null
cat web-logs-raw | grep -e 'coderbyte heroku/router' | grep -v 'MASKED' | grep -oP '(?<=\b\srequest_id=)(\w+\S+)'
cat web-logs-raw | grep -e 'coderbyte heroku/router' | grep 'MASKED' | grep -oP '(?<=\b\srequest_id=)(\w+\S+)' | sed -e 's/$/\ [M]/;'
