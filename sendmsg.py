import pywhatkit as kit
import datetime

message = "سلام نتنااتانانم"
phone_number = "+989111111111"

f = True
while f:
    current_time = datetime.datetime.now()
    hours = current_time.hour
    minutes = current_time.minute + 1  # Send the message 1 minute from now
    print(hours)
    print(minutes)
    
    # Modify the condition based on your specific requirements
    if 6 > 5:
        f = False
        kit.sendwhatmsg(phone_number, message, hours, minutes)
    else:
        f = True




# # Send a WhatsApp Message to a Contact at 1:30 PM
# kit.sendwhatmsg(phone_number, "Hi", 13, 30)

# # Same as above but Closes the Tab in 2 Seconds after Sending the Message
# kit.sendwhatmsg(phone_number, "Hi", 13, 30, 15, True, 2)

# # Send an Image to a Group with the Caption as Hello
# kit.sendwhats_image(phone_number, "Images/Hello.png", "Hello")

# # Send an Image to a Contact with the no Caption
# kit.sendwhats_image(phone_number, "Images/Hello.png")

# # Send a WhatsApp Message to a Group at 12:00 AM
# kit.sendwhatmsg_to_group(phone_number, "Hey All!", 0, 0)

# # Send a WhatsApp Message to a Group instantly
# kit.sendwhatmsg_to_group_instantly(phone_number, "Hey All!")

# # Play a Video on YouTube
# kit.playonyt(phone_number)