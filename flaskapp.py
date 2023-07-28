# This is a simple Flask App to Control Phillips WIZ lights 
# on your network without using an Internet connection.  


from flask import Flask, render_template, request
import socket, time

# IP Addresses of Light Bulbs - Change this to change the IP address of your light bulbs or add/delete them
light_bulb_ips = [ '192.168.1.77', '192.168.1.192']
UDP_PORT = 38899              # UDP Port for Phillips WIZ

# Create a socking object, AF_INET is IPv4, SOCK_DGRAM is UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Utility Fuctions

# Function to send UDP data to Phillips WIZ
def update_light_state(data):
   data = bytes(data, 'utf-8')
   for bulb in light_bulb_ips:
      s.sendto(data, (bulb, UDP_PORT))
      s.sendto(data, (bulb, UDP_PORT))

# Start of Flask App

app = Flask(__name__)

# Default route, display the index.html page
@app.route('/') 
def index():
  return render_template("index.html")

# Hello world, just to test the app
@app.route('/hw') 
def hello_world():
   return 'Hello from Flaskapp!' 

# Send message to turn light on from on button 
@app.route('/on', methods=['POST'])
def wizon():
  data = '{"id":1,"method":"setState","params":{"state":true}}'
  update_light_state(data)
  return ('{"response":"nothing"}')

# Send message to turn light off from off button
@app.route('/off', methods=['POST'])
def wizoff():
  data = '{"id":1,"method":"setState","params":{"state":false}}'
  update_light_state(data)
  return ('{"response":"nothing"}') 
  

# Run through all 32 scenes and play each one for 4 seconds
@app.route('/explode', methods=['POST'])
def wizscenes():
  # Run through all 32 scenes
  for scene in range(0,32):
       data = '{"id":1,"method":"setState","params":{"sceneId":'+str(scene)+'}}'
       update_light_state(data)
       time.sleep(4)
  return ('{"response":"nothing"}') 

# Send message to change the dimmer value from slider
@app.route("/dim/<int:dimmer_value>", methods=['POST','GET'])
def dim(dimmer_value):
   data = '{"id":1,"method":"setState","params":{"dimming":' +str (dimmer_value) +'}}'
   update_light_state(data)
   return ('{"response":"nothing"}')

# Send message to change the color temperature in Kelvin from slider
@app.route("/kelvin/<int:kelvin_value>", methods=['POST','GET'])
def kelvin(kelvin_value):
   data = '{"id":1,"method":"setState","params":{"temp":' +str (kelvin_value) +'}}'
   update_light_state(data)
   return ('{"response":"nothing"}')

# Send message to change to a specific scene 1-32 from buttons
@app.route("/scene/<int:scene_value>", methods=['POST','GET'])
def scene(scene_value):
   data = '{"id":1,"method":"setState","params":{"sceneId":' +str (scene_value) +'}}'
   update_light_state(data)
   return ('{"response":"nothing"}') 

# Send message to change to a specific color using RGB values from slider
@app.route("/color/<rgb>", methods=['POST','GET'])
def color(rgb):
   red, green, blue = [int(x) for x in rgb.split(":")]
   wiz_rgb = '"r":'+str(red)+',"g":' +str(green)+',"b":'+str(blue)
   data = '{"id":1,"method":"setState","params":{'+ wiz_rgb +'}}'
   update_light_state(data)
   return ('{"response":"nothing"}') 

if __name__ == '__main__':
  app.run(debug=True)
