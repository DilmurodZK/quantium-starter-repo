#!/bin/bash
set -e

source venv/bin/activate
pip install -r requirements.txt
pytest tests/ --maxfail=1 --disable-warnings -q
if [ $? -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Some tests failed!"
    exit 1
fi