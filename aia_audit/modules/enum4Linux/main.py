import subprocess
import aia_audit.__main__ as _main
import re

def main(target, settings = None):
    _main.socket.send_message('Starting enum4Linux scanner ...', 'module')
    _main.scan.add_scan_module({"name": "enum4Linux", "devices": []})
    if '/' in target:
        _main.socket.send_message('Scanning for range not implemented yet', 'error')
    else:
        _main.scan.add_scan_device_to_module({"ip": target, "vulnerabilities": []})
        _main.socket.send_message('Scanning IP ' + target + ' with enum4Linux', 'module')
        command = 'enum4linux ' + target
        output = ''
        try:
            output = subprocess.check_output(command, shell=True, encoding="utf-8")
        except subprocess.CalledProcessError as e:
            output = e.output
            pass
        parsed_output = re.sub(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])", "", output)
        _main.scan.add_scan_device_vulnerability({"name": "Scan console output", "description": "Parsed console output from enum4Linux", "severity": "info", "type": "output", "output": parsed_output})
        
