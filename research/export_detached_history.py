"""Export from an ALREADY DETACHED, consistent SQLite backup. Never point at a live production DB.

Usage: python research/export_detached_history.py /path/to/detached.sqlite3 /tmp/history-export.json
The input is opened read-only, immutable, query_only. Output is an independent local file.
This utility neither connects to Railway nor creates a production backup.
"""
import argparse
import json
import sqlite3
from pathlib import Path
from audit_history import audit

def export(detached_db, destination):
    src=Path(detached_db).resolve(strict=True)
    dst=Path(destination).resolve()
    if src==dst: raise ValueError('Destination must differ from source')
    result=audit(src)
    if result['integrity']!='ok': raise ValueError('Source integrity check failed')
    payload={'format':'cryptoscanner-detached-history-audit-v1','source':'operator-supplied-detached-sqlite','audit':result,'limitations':['No live production DB access','Snapshot consistency and provenance must be independently established','Not a raw training data export']}
    dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open('x',encoding='utf-8') as f: json.dump(payload,f,indent=2)
    return dst

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('detached_db');parser.add_argument('destination');args=parser.parse_args();print(export(args.detached_db,args.destination))
