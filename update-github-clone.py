from flask import Flask, request
import os
import hmac
import hashlib
import subprocess

repo_path = '/path/to/repo'
git = '/usr/bin/git'

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/',methods=['POST'])
def handle_webhook():
    if not verify_signature(request.data):
        return "bad signature", 500

    try:
        cmd = ['sudo', '-u', 'www-data', '-H',
                    git, '--git-dir=' + repo_path + '/.git',
                    '--work-tree=' + repo_path,
                    'pull', '--no-edit']
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return str(cmd) + ' failed: ' + str(e.returncode) + '\n' + e.output, 500


def verify_signature(paylod_body):
    h = hmac.new(os.environ['SECRET_TOKEN'], paylod_body, hashlib.sha1)
    signature = 'sha1='+h.hexdigest()
    return signature == request.headers['X-Hub-Signature']

if __name__ == '__main__':
    app.debug = True
    app.run(port=4567)

