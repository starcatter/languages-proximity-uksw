#!/bin/bash
### insert path to java 1.8 installation
#export JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-amd64/"


[ -z "$JAVA_HOME" ] && echo "JAVA_HOME env variable not set!"
PATH=$JAVA_HOME:$PATH
(
cd displayInGraphStream || echo "java sources not found"
mvn clean
mvn package
)
(
cd analyzeAndShow || echo "python sources not found"
if [[ -d venv ]]; then
  source venv/bin/activate
else
  python3 -m venv venv;
  source venv/bin/activate
  pip3 install -r requirements.txt
fi
deactivate
)
