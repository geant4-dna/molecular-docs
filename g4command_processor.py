"""
g4commands_to_markdown.py
Generate markdown from Geant4 commands.

We need these commands from Geant4 at time of writing:
/control/manual /world
/control/manual /analysisDNA
/control/manual /dnageom
/control/manual /cell
"""
import json
import argparse
from os import read
import sys

TYPES = {
    'i': 'int',
    'b': 'bool',
    's': 'str',
    'd': 'double'
}

def read_command_file(infile):
    with open(infile, "r") as ff:
        lines = ff.readlines()

    d = dict()
    inGuidance = False
    current_command = ""
    for line in lines:
        # clean line
        line = line.replace(r"//", "")
        line = line[:-1]
        if line[:24] == r"Command directory path :":
            inGuidance = False
            current_command = ""
        if line[:9] == r"Command /":
            # print(line, file=sys.stderr)
            inGuidance = False
            command = line[9:]
            current_command = command
            d[command] = {"guidance": "", "params": []}
            param_idx = -1
        elif line[:10] == "Guidance :" and current_command != "":
            inGuidance = True
        elif line[:11] == "Parameter :":
            inGuidance = False
            d[current_command]["params"].append({"name": line[12:], "default": "Not Set"})
            param_idx += 1
        elif "Parameter type" in line:
            d[current_command]["params"][param_idx]["type"] = line.split(':')[-1].strip()
            inGuidance = False
        elif "Omittable" in line:
            d[current_command]["params"][param_idx]["omittable"] = line.split(':')[-1].strip()
            inGuidance = False
        elif "Default value" in line:
            d[current_command]["params"][param_idx]["default"] = line.split(':')[-1].strip()
            inGuidance = False
        else:
            if inGuidance is True:
                if d[current_command]["guidance"] == "":
                    d[current_command]["guidance"] += line
                else:
                    d[current_command]["guidance"] += "\n" + line
    return d


def recurse_dictionary(d):
    out = dict()
    for (k, v) in d.items():
        splitkey = k.split(r"/")
        if len(splitkey) > 1:
            key_prefix = "/".join(splitkey[:(len(splitkey) - 1)])
            key_suffix = splitkey[len(splitkey) - 1]
            if key_prefix in out:
                if key_suffix in out[key_prefix]:
                    out[key_prefix][key_suffix].update(v)
                else:
                    out[key_prefix][key_suffix] = v
            else:
                out[key_prefix] = {}
                out[key_prefix][key_suffix] = v
        else:
            if k in out:
                out[k].update(v)
            else:
                out[k] = v

    return out


def to_json(infile):
    a = read_command_file(infile)
    while True in [(r"/" in key) for key in a.keys()]:
        a = recurse_dictionary(a)
    return json.dumps(a, sort_keys=True, indent=2)


def to_markdown(infile):
    """
    Outputs to a HTML table with some Markdown:

    E.g.

    ## /command1
    <table>...</table>

    ## /command2
    <table>...</table>
    ---
    Table columns are
    Command | Description | Parameters
    """
    try:
        import json2html
    except ImportError as err:
        print("This operation requires json2html library, try pip install json2html", file=sys.stderr)
        raise err

    command_dict = read_command_file(infile)
    base_commands = set([k.split('/')[0] for k in command_dict.keys()])
    base_commands = sorted(base_commands)
    # print(base_commands)
    lines = []
    for command in base_commands:
        lines.append(f"## /{command}\n\n")
        sub_commands = [
            {
                "command": key,
                "description": value["guidance"],
                "parameters":  '<ol><li>' + '</li><li>'.join(
                    [f"{param['name']} ({TYPES[param['type']]}, Default: {param['default']}, Omittable: {param['omittable']})"
                        for param in value["params"]]
                ) + '</li></ol>' if len(value["params"]) > 0 else ""
            }
            for key, value in command_dict.items()
            if key.startswith(command)
        ]
        lines.append(json2html.json2html.convert(sub_commands, table_attributes='', escape=False))
        lines.append("\n\n")

    return "\n".join(lines)
    # return json.dumps(sub_commands, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Geant 4 output with commands into a new format (outputs to stream)")
    parser.add_argument('infile')
    parser.add_argument('--json', required=False, action='store_true')
    parser.add_argument('--markdown', required=False, action='store_true')
    parser.add_argument('--raw-json', required=False, action='store_true')

    args = parser.parse_args()
    if args.json and args.markdown:
        print("Cannot have both --json and --markdown set.", file=sys.stderr)
        parser.print_usage()
        sys.exit()
    elif args.json:
        print(to_json(args.infile))
    elif args.raw_json:
        print(json.dumps(read_command_file(args.infile), indent=2))
    elif args.markdown:
        print(to_markdown(args.infile))
    else:
        print("Specify output format")
        parser.print_usage()
        sys.exit()


