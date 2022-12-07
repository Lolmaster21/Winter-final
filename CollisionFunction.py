def collision(pX,pY,CX,CY,CW,CH):#CX and CY are the coordinates of whatevers colliding, CW is width, CH is height
    
    if pX+20 >= CX and pX <= CX+CW and pY+20 >= CY and playerY < CY+CH:
        print("Colliding")
    else:
        print("nah")
