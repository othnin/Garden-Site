from channels import Group

def ws_connect(message):
    print("Someone connected.")
    path = message['path']                                                      # i.e. /sensor/

    if path == b'/garden_site/':
        print("Adding new user to sensor group")
        Group("raspberry_sensor").add(message.reply_channel)                             # Adds user to group for broadcast
        message.reply_channel.send({                                            # Reply to individual directly
           "text": "You're connected to sensor group :) ",
        })
    else:
        print("Strange connector!!")

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    #called whenever the server receives a WebSocket message from a client. 
    print("Received!!" + message['text'])

def ws_disconnect(message):
    print("Someone left us...")
    Group("raspberry_sensor").discard(message.reply_channel)