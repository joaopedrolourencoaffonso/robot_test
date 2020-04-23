from PIL import Image, ImageDraw, ImageFont
import os, random, time

def main():
    #print('hello')
    im = Image.new('RGBA',(200,200),'white')
    draw = ImageDraw.Draw(im)
    fontsFolder='C:\Windows\Fonts'
    arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)

    x = random.randint(100,999)
    y = random.randint(100,999)
    number = str(x) + '' + str(y)
    file = str(number) + ".png"
    x = random.randint(40,60)
    y = random.randint(40,60)
    
    draw.text((x,y),number, fill='black', font=arialFont)
    #im.save('temp.png')
    im.save(file)

    
    print(str(number) + " " + file)








if __name__ == '__main__':
    main()

    
#exemplo de edição de imagem com cor invisivel

#im = Image.open('azul.png')
#    for x in range(50,75):
#        for y in range(50,75):
#            im.putpixel((x,y),(255,0,0,0))

#    im.save('novo.png')



























#import PySimpleGUI as sg

## layout the Window
#layout = [[sg.Text('A custom progress meter')],
#          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
#          [sg.Cancel()]]

## create the Window
#window = sg.Window('Custom Progress Meter', layout)
## loop that would normally do something useful
#for i in range(1000):
#    # check to see if the cancel button was clicked and exit loop if clicked
#    event, values = window.read(timeout=0)
#    if event == 'Cancel' or event is None:
#        break
#        # update bar with loop value +1 so that bar eventually reaches the maximum
#    window['progbar'].update_bar(i + 1)
## done with loop... need to destroy the window as it's still open
#window.close()
