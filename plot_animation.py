import matplotlib.pyplot as plt
from matplotlib import animation

class AnimatePlot:
    
    def __init__(self, data):
        self.fig = plt.figure()
        self.axis = plt.axes(xlim =(-50, 50),
                        ylim =(-50, 50)) 
        self.line, = self.axis.plot([], [], lw = 2)
        self.xdata, self.ydata = [], []
        self.data = data
        return None
        
    def init(self): 
        self.line.set_data([], []) 
        return self.line, 
    
    def animate(self, i): 
        # t is a parameter which varies
        # with the frame number
        t = i 
        
        # x, y values to be plotted 
        x = t
        y = self.data[x]
        
        # appending values to the previously 
        # empty x and y data holders 
        self.xdata.append(x) 
        self.ydata.append(y) 
        self.line.set_data(self.xdata, self.ydata) 
        
        return self.line,
    
    def animate_plot(self):
        anim = animation.FuncAnimation(
            self.fig, self.animate, init_func = self.init, 
            frames = 500, interval = 20, blit = True)
        return anim
    
    def save_animation(self, anim, path_file:str=None):
        path_file = 'test_file.mp4' if not path_file else path_file
        anim.save(path_file, writer = 'ffmpeg', fps = 30)
        return f'animation is written to {path_file}'
    
if __name__ == '__main__':
    import numpy as np
    
    mydata = [np.sin(idx) for idx in range(500)] 
    path_dir = '/Users/pinaki/Library/CloudStorage/OneDrive-Personal/Documents/Analytics_Projects/algos_from_scratch/'
    obj = AnimatePlot(mydata)
    anim = animation.FuncAnimation(
        obj.fig, obj.animate, init_func = obj.init, 
        frames = 500, interval = 20, blit = True)
    # anim.save(path_dir + 'sample_animated_plot.mp4', writer = 'ffmpeg', fps = 30)
    plt.show()