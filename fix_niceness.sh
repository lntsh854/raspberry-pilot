#!/bin/bash
sudo renice -n -5 `ps -C boardd -o pid= `
sudo renice -n -4 `ps -C controlsd -o pid= `
sudo renice -n -3 `ps -C dashboard -o pid= `
sudo renice -n -2 `ps -C influxd -o pid= `
sudo renice -n -1 `ps -C transcoderd -o pid= `
