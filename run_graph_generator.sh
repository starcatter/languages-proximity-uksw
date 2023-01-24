#!/bin/bash
### insert path to java 1.8 installation
#export JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-amd64/"

(
cd analyzeAndShow ||  (echo "python sources not found"; exit)
source venv/bin/activate
cd ..
python3 -m analyzeAndShow.graph_generator "$@"
deactivate
)
