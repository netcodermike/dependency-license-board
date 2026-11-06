# Using Dependency License Board

## Quick start

Run `python app.py /path/to/project`. It reads only direct package.json/requirements.txt and root LICENSE/COPYING/NOTICE files. It performs no network lookup or package installation. Unknown licenses remain unknown.

## Supported workflow

1. Direct npm/Python requirement inventory.
2. Local license/notice evidence excerpts.
3. Unknown-license and unsupported-directive reporting.

## Validation and troubleshooting

Run the commands in the README. Invalid inputs produce explicit errors rather than silently changing the requested operation. Browser audio requires a user gesture; microphone apps require HTTPS or localhost and permission. For file tools, supply supported input formats and writable output directories.

## Limitations

Does not resolve transitive dependencies or infer legal license compatibility. Review actual package license evidence before distribution.

Tests use synthetic fixtures. These tests do not certify hardware compatibility, real-world forecast quality, trained-model accuracy, or production suitability for every input.
