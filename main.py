import os
import eiscp

from flask import Flask, jsonify, request

app = Flask(__name__)
ip = os.environ.get('ONKYO_IP')
print(ip)

@app.route('/receiver', methods=['GET'])
def receiver():
    volume = request.args.get('volume')
    power = request.args.get('power')
    
    text = 'Hello World!'

    if volume is not None:
        with eiscp.eISCP(ip) as receiver:
            floatVolume = float(volume)
            if floatVolume < 80:
                volume = '0' + volume
                intVolume = int(floatVolume)
                strVolume = str(intVolume)
                receiver.command('volume ' + strVolume)
                text = 'Volume ' + strVolume + '!'
    if power == "on":
        with eiscp.eISCP(ip) as receiver:
            receiver.command('power on')
            text = 'Power ON!'
    if power == "off":
        with eiscp.eISCP(ip) as receiver:
            receiver.command('power off')
            text = 'Power OFF!'
    print(text)
    return jsonify({'message': text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)