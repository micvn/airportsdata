"""Updates counts in readme.rst file.  Requires Python >= 3.10."""
from pathlib import Path

import airportsdata

icao_count = len(airportsdata.load('ICAO'))
iata_count = len(airportsdata.load('IATA'))
lid_count = len(airportsdata.load('LID'))
iata_macs_count = len(airportsdata.load_iata_macs())
IATA_MACs_apts_count = sum(len(a['airports']) for a in airportsdata.load_iata_macs().values())

readme_file = Path('README.rst')
readme = readme_file.read_text()
out_lines = readme.splitlines(keepends=True)
for i, line in enumerate(out_lines):
    if line.startswith('.. |ICAO| replace::'):
        out_lines[i] = f'.. |ICAO| replace:: {icao_count:,}\n'
    elif line.startswith('.. |IATA| replace::'):
        out_lines[i] = f'.. |IATA| replace:: {iata_count:,}\n'
    elif line.startswith('.. |LID| replace::'):
        out_lines[i] = f'.. |LID| replace:: {lid_count:,}\n'
out = ''.join(out_lines)
if out != readme:
    print(f'Updated counts in README.rst to ICAO={icao_count:,}, IATA={iata_count:,} and LID={lid_count:,}')
    readme_file.write_text(out, newline='\n')
else:
    print(f'No changes to counts in README.rst: ICAO={icao_count:,}, IATA={iata_count:,} and LID={lid_count:,}')

readme_file = Path('README_IATA.rst')
readme = readme_file.read_text()
out_lines = readme.splitlines(keepends=True)
for i, line in enumerate(out_lines):
    if line.startswith('.. |IATA_MACs| replace::'):
        out_lines[i] = f'.. |IATA_MACs| replace:: {iata_macs_count:,}\n'
    if line.startswith('.. |IATA_MACs_apts| replace::'):
        out_lines[i] = f'.. |IATA_MACs_apts| replace:: {IATA_MACs_apts_count:,}\n'
out = ''.join(out_lines)
if out != readme:
    print(
        f'Updated counts in README_IATA.rst to IATA_MACs={iata_macs_count:,} and '
        f'IATA_MACs_apts={IATA_MACs_apts_count:,}'
    )
    readme_file.write_text(out, newline='\n')
else:
    print(
        f'No changes to counts in README_IATA.rst: IATA_MACs={iata_macs_count:,} and '
        f'IATA_MACs_apts={IATA_MACs_apts_count:,}'
    )
