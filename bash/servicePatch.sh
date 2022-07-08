#!/bin/bash

# Simple script to apply appProtocol: http field at each service into the mesh

CLIENT="oc"
NAMESPACE="default"

i=0
while [[ i -lt $# ]]; do
  i=$((i+1))
  FLAG="$(cut -d ' ' -f $i <<< $@)"
  i=$((i+1))
  FVALUE="$(cut -d ' ' -f $i <<< $@)" 
  echo -e "[i] Parse ${FLAG} ${FVALUE}"
  case $FLAG in
    "-ns" | "--namespace")
      NAMESPACE=$FVALUE
    ;;
    *)
        echo "not found"
    ;;
  esac
done

for svc in $($CLIENT -n $NAMESPACE get svc | cut -d " " -f 1 | tail -n +2)
do 
  echo "[i] Patch $svc file..."
  ports=$($CLIENT -n $NAMESPACE get svc $svc -o jsonpath="{.spec.ports}" | jq '.[0] += {"appProtocol": "http"}')
  patch="{\"spec\":{\"ports\":$ports}}"
  echo $patch
  $CLIENT -n $NAMESPACE patch svc $svc -p "$patch"

done