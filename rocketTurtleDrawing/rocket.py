from turtle import *

color('grey')
begin_fill()
while True:
    forward(200)
    left(20)
    if abs(pos()) < 1:
        break
end_fill()
done()