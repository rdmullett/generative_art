import random

# 8x10 at 300 DPI: 
w, h = 2551, 3295
#w, h = 1000, 1000

colors = [(242, 231, 80), (242, 184, 7), (242, 135, 5), (197, 33, 4), (113, 3, 1)]

def color():
    number = random.randint(0, 4)
    color = stroke(colors[number][0],colors[number][1],colors[number][2])
    return color

def circular(circle_list):
    circle(circle_list[0], circle_list[1], circle_list[2])

def setup():
    size(w, h)
    background(255)
    strokeWeight(500)
    circles = []
    #blendMode(DIFFERENCE)
    locations = []
    
    #for i in range(63):
    for dist_x in range(7):
        for dist_y in range(9):
            location = (dist_x+1)*350, (dist_y+1)*350
            locations.append(location)
    print(locations)

    for i in range(len(locations)):
        location = locations[i]
        #location = [random.randint(0, w-50), random.randint(0, h-50)]
        initialweight = 500 #random.randint(400, 10000)
        weight = initialweight
        #weight = random.randint(500)
        col_iter = 4
        for i in range(5):
            strokeWeight(weight)
            current_color = colors[col_iter]
            stroke(current_color[0], current_color[1], current_color[2])
            fill(current_color[0], current_color[1], current_color[2])

            circle_list = [location[0], location[1], 200]
            circular(circle_list)
            col_iter -= 1
            weight -= initialweight/4
        
    save("output.png")

    
