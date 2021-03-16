#!/usr/bin/env python3

import sys
from typing import TextIO, Dict, Any, List
import re

Command = Dict[str, Any]


def parse_commands(infile: TextIO) -> List[Command]:
    commands = []
    command: Command = {}
    type_ = 'unknown'
    code_parsed = False
    for line in infile:
        line = line.strip()

        if re.match(r'^## Master → Slave', line):
            type_ = 'mosi'
        if re.match(r'^## Slave → Master', line):
            type_ = 'miso'

        try:
            match = re.match(r'^### `(0x..)` (.*) <a name="(.*)">', line)
            if match:
                if command != {}:
                    assert code_parsed
                    commands.append(command)
                code, name, link = match.groups()
                intcode = int(code, base=16)
                code_parsed = False
                command = {}
                command['code'] = intcode
                command['name'] = name
                command['type'] = type_
                command['link'] = link

            match = re.match(r'^\* Command type: (.*)\.$', line)
            if match:
                command['mositype'] = match.group(1)

            match = re.match(r'^\* Command Code byte: `(0x..)`', line)
            if match:
                assert int(match.group(1), base=16) == command['code'], \
                    f'{match.group(1)} != {command["code"]}'
                code_parsed = True

            match = re.search(r'[Aa]bbreviation: `(.*)`', line)
            if match:
                command['abbreviation'] = match.group(1)

            match = re.match(r'^\* N.o. data bytes: \*?(.*?)\*?\.', line)
            if match:
                command['data_bytes'] = match.group(1)

            if line.startswith('* Response:'):
                match = re.findall(r'\[\*?(.*?)\*?\]\(#(.*?)\)', line)
                command['responses'] = match if match else []

            if line.startswith('* Command type:'):
                command['address'] = 'specific module' in line
                command['broadcast'] = 'broadcast' in line

        except Exception:
            print(f'Failed on command: {command}')
            raise


    if command != {}:
        assert code_parsed
        commands.append(command)

    return commands


def gen_summary(commands: List[Command], ostream: TextIO) -> None:
    ostream.write('# Commands summary\n\n')

    ostream.write('## Master → Slave\n\n')
    mosi = list(filter(lambda command: command['type'] == 'mosi', commands))
    gen_table(mosi, ostream)
    ostream.write('\n\n')

    ostream.write('## Slave → Master\n\n')
    miso = list(filter(lambda command: command['type'] == 'miso', commands))
    gen_table(miso, ostream)


def gen_table(commands: List[Command], ostream: TextIO) -> None:
    ostream.write('<table>\n')
    ostream.write(
        '<tr>'
        '<th>Command</th>'
        '<th>Code byte</th>'
        '<th>Abbreviation</th>'
    )
    if 'responses' in commands[0]:
        ostream.write('<th>Response</th>')
    if 'broadcast' in commands[0]:
        ostream.write('<th>Addressed</th>')
    ostream.write('</tr>\n')

    for command in commands:
        try:
            gen_table_line(command, ostream)
        except Exception:
            print(f'Generating table failed for command: {command}')
            raise

    ostream.write('</table>\n')


def gen_table_line(command: Command, ostream: TextIO) -> None:
    if 'responses' in command:
        responses = ', '.join(
            f'<a href="commands.md#{link}">{name}</a>' for name, link in command['responses']
        )
        if responses == '':
            responses = '–'

    ostream.write('<tr>\n')
    ostream.write(f' <td><a href="commands.md#{command["link"]}">{command["name"]}</a></td>\n')
    ostream.write(f' <td><code>{hex(command["code"])}</code></td>\n')
    ostream.write(f' <td><code>{command["abbreviation"]}</code></td>\n')
    if 'responses' in command:
        ostream.write(f' <td>{responses}</td>\n')
    if 'broadcast' in command and 'address' in command:
        type_ = []
        if command['address']:
            type_.append('address')
        if command['broadcast']:
            type_.append('broadcast')
        type_ = ', '.join(type_)
        ostream.write(f' <td>{type_}</td>\n')
    ostream.write('</tr>\n')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: commands_create_summary.py commands.md '
                         '[outputfile.md]\n')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as infile:
        outfile = open(sys.argv[2], 'w', encoding='utf-8') \
                  if len(sys.argv) > 2 else sys.stdout

        commands = parse_commands(infile)
        gen_summary(commands, outfile)
