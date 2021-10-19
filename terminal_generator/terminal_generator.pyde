w, h = 1920, 1080
import random
#retro rainbow color palette
background_colors = [(3, 19, 38), (23, 44, 66), (47, 68, 92), (73, 93, 117), (3, 33, 35), (220, 226, 232)]

colors = [(10, 123, 131),(42, 168, 118),(255, 210, 101),(241, 156, 101),(206, 77, 69)]
colors2 = [(255, 204, 13), (255, 115, 38), (255, 25, 77), (191, 38, 105), (112, 42, 140)]
#colors3 = [(75, 56, 94), (0, 127, 148), (238, 215, 141), (194, 43, 38), (255, 182, 50)]
#colors4 = [(76, 100, 114), (87, 164, 177), (176, 216, 148), (250, 222, 137), (249, 83, 85)]
#color_lists = [colors, colors2, colors3, colors4]
color_lists = colors, colors2

def background_color():
    number = random.randint(0, 5)
    color = fill(background_colors[number][0], background_colors[number][1], background_colors[number][2])

def color(color_list):
    number = random.randint(0, 4)
    color = stroke(color_list[number][0],color_list[number][1],color_list[number][2])

def terminal(number_of_terminals, w, h):
    terminal_number = 0
    while terminal_number < number_of_terminals:
        strokeWeight(2)
        
        terminal_Xstart = random.randint(0, w/1.5)
        terminal_Xend = terminal_Xstart + random.randint(250, w)
        
        terminal_Ystart = random.randint(0, h/1.5)
        terminal_Yend = terminal_Ystart + random.randint(250, h)
        
        stroke(255)
        fill(255)
        rect(terminal_Xstart, terminal_Ystart, terminal_Xend, terminal_Yend, 15)
        background_color()
        rect(terminal_Xstart, terminal_Ystart+25, terminal_Xend, terminal_Yend, 0, 0, 15, 15)
        
        #top circles:
        noStroke()
        fill(colors[4][0],colors[4][1],colors[4][2])
        circle(terminal_Xstart+15, terminal_Ystart+15, 15)
        fill(colors[2][0],colors[2][1],colors[2][2])
        circle(terminal_Xstart+35, terminal_Ystart+15, 15)
        fill(colors[3][0],colors[3][1],colors[3][2])
        circle(terminal_Xstart+55, terminal_Ystart+15, 15)
        
        starting_loc = terminal_Ystart + 45
        ending_loc = terminal_Ystart + terminal_Yend
        current_loc = starting_loc
        
        line_break_chance = .1
        indent_chance = .4
        indent_distance = 60
        line_break = False
        current_indent = 0
        #color_list = color_lists[random.randint(0,3)]
        color_list = color_lists[random.randint(0,1)]


        
        strokeWeight(10)    
        #iterate over the size of the terminal and generate lines of code
        while(current_loc < ending_loc):
            color(color_list)
            line_break_chance_test = random.random()
            #check if we should line break, and if indent is 0 we do this:
            if (not (line_break_chance_test < line_break_chance) and current_indent is 0):
                line_break = False 
                #TODO: make proper indentation and proper line length
                line_start = terminal_Xstart + 15
                line_length = random.randint(line_start+60, terminal_Xstart+terminal_Xend-15)
                line(line_start, current_loc, line_length, current_loc)
                if (not (random.random() < indent_chance)):
                    current_indent += 1
                    current_loc += 25
                else:
                    current_loc += 25
            #check if we should line break if indent isn't 0
            elif (not (line_break_chance_test < line_break_chance)):
                line_break = False
                line_start = terminal_Xstart + 15 + (current_indent * indent_distance)
                line_end = random.randint(line_start+50, terminal_Xstart+terminal_Xend-15)
                line(line_start, current_loc, line_end, current_loc)
                if current_indent > 4:
                    current_indent = 0
                    current_loc += 25
                elif (not (random.random() < indent_chance)):
                    current_indent += 1
                    current_loc += 25
                else:
                    current_loc += 25
            #otherwise, if line_break_chance_test is less than the threshhold we break
            else:
                #line break
                current_loc += 25
                line_break = True
        
        terminal_number += 1

def setup():
    background(89)
    stroke(255)
    strokeWeight(2)
    size(w, h)
    number_of_terminals = random.randint(1, 6)
    
    terminal(number_of_terminals, w, h)
    save(str(random.randint(0, 1000))+"_output.png")
