#!/bin/bash

java \
  -Djava.library.path=. \
  -classpath '*' \
  org.mozilla.javascript.tools.shell.Main $*