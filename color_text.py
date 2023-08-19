class ColorText:
    def text_in_color(txt:str, color_font_name:str=None, color_bg_name:str=None, style_name:str='normal'):
        '''
        output the text with a foreground and a background color
        args:
            `txt`(str): text to be printed
            `color_font_name`(str): font color amongst ['black', 'red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'grey']
            `color_bg_name`(str): back ground color amongst ['black', 'red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'grey']
            `style_name`(str): ['normal', 'bold', 'light', 'italics', 'underline', 'blink']
        '''
        colors = ['black', 'red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'grey']
        dict_color_map_font = {k:v for k,v in zip(colors, range(30,38))}
        dict_color_map_bg = {k:v for k,v in zip(colors, range(40,48))}
        dict_styles = {'normal':0, 'bold':1, 'light':2, 'italics':3, 'underline':4, 'blink':5}
        color_font = dict_color_map_font.get(color_font_name, 30)
        color_bg = dict_color_map_bg.get(color_bg_name, 49)
        style_font = dict_styles.get(style_name, 0)

        txt_w_col = f"\x1b[{style_font};{color_font};{color_bg}m{txt}"

        return txt_w_col

    def text_to_green(txt:str):
        txt_w_col = ColorText.text_in_color(txt, 'green')
        return txt_w_col

    def text_to_red(txt:str):
        txt_w_col = ColorText.text_in_color(txt, 'red')
        return txt_w_col