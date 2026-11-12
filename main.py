from __future__ import annotations
def run(lines):
 import json
 return [json.loads(s) for s in lines if s.strip()]
