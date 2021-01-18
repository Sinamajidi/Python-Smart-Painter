# Used Libraries Import Section:
import pyautogui
from PIL import Image
from random import randrange
from keyboard import is_pressed
from sys import platform
from os import path, system


# Calculating File Directory ( dir+/ ):
file_dir = str(path.dirname(path.realpath(__file__)))
if '\\' in file_dir:
    file_dir = file_dir.replace('\\', '/')+'/'
else:
    file_dir = file_dir + '/'


# Checking Supported Operating System (Windows):
if platform != "win32":
    pyautogui.alert(title="Python Painter Error",
                    text="This Program isn't Available for non-windows OS Yet")
    exit()
else:
    system('title Python')


# RGB to Hexadecimal Function:
def rgb2hex(r, g, b):
    return '%02x%02x%02x' % (r, g, b)


# Paint3D Minimum and Maximum position Of Frame:
# minn = x:119 y:247
# maxn = x:1536  y:960


# Defining Frame Size And Painting Padding:
frame = [[119, 247], [1536, 960]]
width_Padding = frame[0][0] + 1
height_Padding = frame[0][1] + 3


# Calculating Paint3D Width And Height:
frame_width = frame[1][0] - frame[0][0]
frame_height = frame[1][1] - frame[0][1]


# Waiting For Image Path :
image_loc = pyautogui.prompt(
    text='Enter image path:', title='Python Painter Prompt', default='')


# Check If Image Path Has Invalid Form:
while True:

    if image_loc == '' or path.exists(image_loc) == False or str(image_loc).replace(' ', '') == '':
        print('File Location Invalid.')
        image_loc = pyautogui.prompt(
            text='Enter [Correct] image path:', title='Python Painter Prompt', default=str(image_loc))

    if image_loc != '' and str(image_loc).replace(' ', '') != '' and path.exists(image_loc) == True:
        print('File Location Found.')
        Image_M = image_loc
        break

# Opening Image And Converting to RGB:
im = Image.open(Image_M)
rgb_im = im.convert('RGB')


# Waiting For Selecting Painting Software :
selected_program = pyautogui.prompt(
    text='Select the program you want to use:\n[1] - Paint\n[2] - Paint3D', title='Python Painter Prompt', default='')


# Main Check Of Selected Software:
while True:
    if str(selected_program) == '1' or str(selected_program) == '2' or str(selected_program).lower() == 'paint' or str(selected_program).lower() == 'paint3d':
        if str(selected_program) == '1' or str(selected_program).lower() == 'paint':
            print('Paint Software Has Been Selected.')
            if im.size[0] > frame_width or im.size[1] > frame_height:
                print('Image Size Error (Width/Height > Paint3d/Paint Board)')
                exit()

            # Notice Message Box:
            pyautogui.alert(title="Python Painter Notice", text="""1-Make Sure That You Are Using Your Selected Painting Software in Full-Screen Mode. (This Can Prevent Clicking Incorrect Positions)

            2-You Can Exit The Program By holding "q" or "p" on the keyboard for 2 seconds
                                """)

            # Check the Target Software Opened Window:
            get_windows = pyautogui.getWindowsWithTitle("paint")
            if len(get_windows) != 0:
                for window in get_windows:
                    if window.isMaximized == False:
                        window.maximize()
                        break
                    else:
                        break

                # Alert On Not Found:
                if len(get_windows) == 0:
                    pyautogui.alert(title="Python Painter Alert",
                                    text="No opened window than Painter Software Found. Please Open Paint Software.")
                    exit()

            # Get the start command:
            starter = pyautogui.confirm(title='Python Painter Check',
                                        text='Are You Ready To Start?', buttons=['Yes', 'No'])

            # Cancellation Alert:
            if starter == 'No':
                print('Program Canceled By User.')
                pyautogui.alert(title='Python Painter Alert',
                                text='Program Canceled')
                exit()

            # Get Ready Alert:
            else:
                pyautogui.alert(title='Python Painter Alert',
                                text='The program was delayed for 3 seconds... Get Ready!', timeout=3000)

            while True:

                Edit_Colors = pyautogui.locateCenterOnScreen(
                    file_dir+'Assets/Paint/Edit_Colors.png')
                if Edit_Colors != None:

                    pyautogui.click(Edit_Colors[0], Edit_Colors[1])

                    while True:
                        R_G_B = pyautogui.locateCenterOnScreen(
                            file_dir+'Assets/Paint/R_G_B.png')
                        if R_G_B != None:
                            count = 0
                            last = []
                            while count != im.size[1]-1:
                                for w_p in range(0, im.size[0]):
                                    for h_p in range(0, im.size[1]):
                                        pyautogui.FAILSAFE = True
                                        if len(last) >= 1:
                                            last_hex = last[len(last)-1]

                                            rr, gg, bb = rgb_im.getpixel(
                                                (w_p, h_p))

                                            if [rr, gg, bb] != last_hex:
                                                pyautogui.click(
                                                    Edit_Colors[0], Edit_Colors[1])

                                                pyautogui.moveTo(
                                                    R_G_B[0]+45, R_G_B[1]-17)
                                                pyautogui.doubleClick(
                                                    R_G_B[0]+45, R_G_B[1]-17)

                                                pyautogui.write(str(rr))

                                                pyautogui.moveTo(
                                                    R_G_B[0]+45, R_G_B[1]+5)
                                                pyautogui.doubleClick(
                                                    R_G_B[0]+45, R_G_B[1]+5)

                                                pyautogui.write(str(gg))

                                                pyautogui.moveTo(
                                                    R_G_B[0]+45, R_G_B[1]+26)
                                                pyautogui.doubleClick(
                                                    R_G_B[0]+45, R_G_B[1]+26)

                                                pyautogui.write(str(bb))

                                                pyautogui.click(
                                                    R_G_B[0]-336, R_G_B[1]+52)

                                        else:
                                            rr, gg, bb = rgb_im.getpixel(
                                                (w_p, h_p))

                                            pyautogui.moveTo(
                                                R_G_B[0]+45, R_G_B[1]-17)
                                            pyautogui.doubleClick(
                                                R_G_B[0]+45, R_G_B[1]-17)

                                            pyautogui.write(str(rr))

                                            pyautogui.moveTo(
                                                R_G_B[0]+45, R_G_B[1]+5)
                                            pyautogui.doubleClick(
                                                R_G_B[0]+45, R_G_B[1]+5)

                                            pyautogui.write(str(gg))

                                            pyautogui.moveTo(
                                                R_G_B[0]+45, R_G_B[1]+26)
                                            pyautogui.doubleClick(
                                                R_G_B[0]+45, R_G_B[1]+26)

                                            pyautogui.write(str(bb))

                                            pyautogui.click(
                                                R_G_B[0]-336, R_G_B[1]+52)

                                        pyautogui.FAILSAFE = False
                                        pyautogui.moveTo(0, 0)

                                        pyautogui.click(width_Padding+w_p,
                                                        height_Padding+h_p)
                                        count += 1
                                        last.append([rr, gg, bb])

                                        # Displaying Details:
                                        print('-----------------------')
                                        print('Pixel Position:',
                                              w_p, count)
                                        print('Red:', str(rr), 'Green:',
                                              str(gg), 'Blue:', str(bb))

                                        print('-----------------------')

                                        # Scheduled Exit:
                                        # if w_p == 200 and h_p == 200:
                                        #     exit()

                                        # Alert On Done:
                                        if w_p == im.size[0] and h_p == im.size[1]:
                                            print('\nProcess Done!')
                                            Done = pyautogui.alert(
                                                title='Python Painter Alert', text='Painting Successfully Done.')
                                            if Done == 'OK':
                                                exit()

                                        # Exit with Pressing "q":
                                        if keyboard.is_pressed("q"):
                                            print(
                                                'Keyboard interrupt: Pressed "q"')
                                            exit()

                                        # Exit with Pressing "p":
                                        if keyboard.is_pressed("p"):
                                            print(
                                                'Keyboard interrupt: Pressed "p"')
                                            exit()
        elif str(selected_program) == '2' or str(selected_program).lower() == 'paint3d':
            print('Paint3D Software Has Been Selected.')

            if im.size[0] > frame_width or im.size[1] > frame_height:
                print('Image Size Error (Width/Height > Paint3d Board)')
                exit()

            # Notice Message Box:
            pyautogui.alert(title="Python Painter Notice", text="""1-Make Sure That You Are Using Your Selected Painting Software in Full-Screen Mode. (This Can Prevent Clicking Incorrect Positions)

            2-You Can Exit The Program By holding "q" or "p" on the keyboard for 2 seconds
                                """)

            # Check the Target Software Opened Window:
            get_windows = pyautogui.getWindowsWithTitle("paint 3d")
            if len(get_windows) != 0:
                for window in get_windows:
                    if window.isMaximized == False:
                        window.maximize()
                        break
                    else:
                        break

                # Alert On Not Found:
                if len(get_windows) == 0:
                    pyautogui.alert(title="Python Painter Alert",
                                    text="No opened window than Painter Software Found. Please Open Paint 3D Software.")
                    exit()

            # Get the start command:
            starter = pyautogui.confirm(title='Python Painter Check',
                                        text='Are You Ready To Start?', buttons=['Yes', 'No'])

            # Cancellation Alert:
            if starter == 'No':
                print('Program Canceled By User.')
                pyautogui.alert(title='Python Painter Alert',
                                text='Program Canceled')
                exit()
            else:

                # Get Ready Alert:
                pyautogui.alert(title='Python Painter Alert',
                                text='The program was delayed for 3 seconds... Get Ready!', timeout=3000)

            while True:

                Color_1 = pyautogui.locateCenterOnScreen(
                    file_dir+'Assets/Paint3D/Color_i.png')

                New_BTN = pyautogui.locateCenterOnScreen(
                    file_dir+'Assets/Paint3D/New_BTN.png')
                if New_BTN != None:
                    pyautogui.click(New_BTN[0], New_BTN[1])

                if Color_1 != None:

                    pyautogui.click(Color_1[0]-150, Color_1[1])

                    while True:
                        Color_2 = pyautogui.locateCenterOnScreen(
                            file_dir+'Assets/Paint3D/Color_ii.png')
                        if Color_2 != None:
                            count = 0
                            last = []
                            while count != im.size[1]-1:
                                for w_p in range(0, im.size[0]):
                                    for h_p in range(0, im.size[1]):
                                        pyautogui.FAILSAFE = True
                                        if len(last) >= 1:
                                            last_hex = last[len(last)-1]

                                            rr, gg, bb = rgb_im.getpixel(
                                                (w_p, h_p))
                                            pixel_hex = rgb2hex(rr, gg, bb)

                                            if str(pixel_hex) != str(last_hex):
                                                pyautogui.click(
                                                    Color_1[0]-150, Color_1[1])
                                                pyautogui.moveTo(
                                                    Color_2[0]+170, Color_2[1]-50)
                                                pyautogui.click(
                                                    Color_2[0]+170, Color_2[1]-50)

                                                pyautogui.write(
                                                    str(pixel_hex))

                                                pyautogui.press('Enter')
                                                pyautogui.click(
                                                    Color_2[0]-100, Color_2[1])
                                        else:
                                            rr, gg, bb = rgb_im.getpixel(
                                                (w_p, h_p))
                                            pixel_hex = rgb2hex(rr, gg, bb)

                                            pyautogui.click(
                                                Color_1[0]-150, Color_1[1])
                                            pyautogui.moveTo(
                                                Color_2[0]+170, Color_2[1]-50)
                                            pyautogui.click(
                                                Color_2[0]+170, Color_2[1]-50)

                                            pyautogui.write(str(pixel_hex))

                                            pyautogui.press('Enter')
                                            pyautogui.click(
                                                Color_2[0]-100, Color_2[1])

                                        pyautogui.FAILSAFE = False
                                        pyautogui.moveTo(0, 0)

                                        pyautogui.click(width_Padding+w_p,
                                                        height_Padding+h_p)
                                        count += 1
                                        last.append(pixel_hex)

                                        # Displaying Details:
                                        print('-----------------------')
                                        print('Pixel Position:',
                                              w_p, count)
                                        print('Red:', str(rr), 'Green:',
                                              str(gg), 'Blue:', str(bb))
                                        print('Hex:', str(pixel_hex))
                                        print('-----------------------')

                                        # Scheduled Exit:
                                        # if w_p == 200 and h_p == 200:
                                        #     exit()

                                        # Alert On Done:
                                        if w_p == im.size[0] and h_p == im.size[1]:
                                            print('\nProcess Done!')
                                            Done = pyautogui.alert(
                                                title='Python Painter Alert', text='Painting Successfully Done.')
                                            if Done == 'OK':
                                                exit()

                                        # Exit with Pressing "q":
                                        if keyboard.is_pressed("q"):
                                            print(
                                                'Keyboard interrupt: Pressed "q"')
                                            exit()

                                        # Exit with Pressing "p":
                                        if keyboard.is_pressed("p"):
                                            print(
                                                'Keyboard interrupt: Pressed "p"')
                                            exit()

    # Checking If Input Format Has Invalid Form:
    else:
        print('Selected Program Input Invalid.')
        selected_program = pyautogui.prompt(
            text='Select the program you want to use:\n[1] - Paint\n[2] - Paint3D', title='Python Painter Prompt', default='')
