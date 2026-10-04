# Autonomous change agent

The agent may diagnose misses and propose/edit challenger code. It may not directly overwrite production, signing material, or secrets. Every change must pass deterministic tests, regression checks and prospective shadow comparison before the promotion controller can create a release candidate. Model providers are replaceable; the scanner remains operational when no model provider is configured.
