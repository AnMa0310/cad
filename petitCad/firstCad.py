# this is for cad 
# reference : https://imagingsolution.net/program/python/tkinter/canvas_drawing_lines_circles_shapes/
# reference : https://water2litter.net/rum/post/python_tkinter_canvas_draw/
# reference : https://teratail.com/questions/161471
# reference : https://qiita.com/chihiro1364/questions/d818136af98b8837cbc0

import tkinter as tk

class node:
    x = 0
    y = 0


class DrawLine(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        canvas1 = tk.Canvas(self, width=400, height=500, bg="white")
        canvas1.pack(fill=tk.BOTH, expand=True)

#        canvas1.create_line(40, 20, 200, 400, fill="Magenta", width=2)

        nodes = []
        lines = []

        def drag(event):
            canvas1.delete("line")
            node.x = event.x
            node.y = event.y
            updatecoord()
            if len(nodes)>0:
                canvas1.create_line(nodes[-2], nodes[-1], event.x, event.y, fill="cyan", tag="line", width=2)

        def updatecoord():
#            textnode = "X={} Y={}".format(node.x, node.y)
            textnode = f"X={node.x} Y={node.y}"
            canvas1.delete(tag1)
            canvas1.create_text(20, 10, fill="magenta", text=textnode, tag=tag1, anchor="nw")

        def clickleft(event):
            nodes.append(event.x)
            nodes.append(event.y)
            canvas1.create_oval(event.x-4, event.y-4, event.x+4, event.y+4, outline="purple", fill="magenta")
            textnode = f"X={node.x} Y={node.y}"
#            canvas1.create_text(node.x, node.y, fill="blue", text=textnode, tag=tag1)
            canvas1.create_text(node.x+5, node.y-5, fill="blue", text=textnode, anchor="sw")
            if len(nodes)>2:
                canvas1.create_line(nodes[-4], nodes[-3], event.x, event.y, fill="blue", width=2)

        def clickright(event):
            lines.append(nodes)
            nodes.clear()

        canvas1.bind('<Motion>', drag)
        canvas1.bind('<Button-1>', clickleft)
        canvas1.bind('<Button-3>', clickright)

root1 = tk.Tk()
root1.title("Test0006")
tag1="motion_up"
main1 = DrawLine(master=root1)
main1.mainloop()