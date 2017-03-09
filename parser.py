from display import *
from matrix import *
from draw import *
import time

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single word that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing
See the file script for an example of the file format
"""

bubble = ["ident", "apply", "display"]
tea = ["line", "scale", "move", "rotate", "save"]

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r');
    temp = f.read().split("\n");
    ctr = 0;
    while (ctr < len(temp)-1):
        tmp = temp[ctr]
        if tmp in bubble:
            if tmp == "ident":
                ident(transform);
            if tmp == "apply":
                matrix_mult(transform, points);
            if tmp == "display":
                clear_screen(screen);
                draw_lines(points, screen, color);
                display(screen);
                time.sleep(1)
            ctr+=1;
        elif tmp in tea:
            args = temp[ctr+1].split(" ");
            if tmp == "line":
                add_edge(points, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]));
            if tmp == "scale":
                scaletrix = make_scale(float(args[0]), float(args[1]), float(args[2]));
                matrix_mult(scaletrix, transform);
            if tmp == "move":
                trantrix = make_translate(float(args[0]), float(args[1]), float(args[2]));
                matrix_mult(trantrix, transform);
            if tmp == "rotate":
                if args[0] == "x":
                    rotrix = make_rotX(float(args[1]));
                if args[0] == "y":
                    rotrix = make_rotY(float(args[1]));
                if args[0] == "z":
                    rotrix = make_rotZ(float(args[1]));
                matrix_mult(rotrix, transform);
            if tmp == "save":
                clear_screen(screen);
                draw_lines(points, screen, color);
                save_extension(screen, args[0]);
                time.sleep(1)
            ctr+=2;
        else:
            ctr+=1
