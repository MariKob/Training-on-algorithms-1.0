a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == 0:
    if b == 0:
        if e == 0:
            if d == 0:
                if c == 0:
                    if f == 0:
                        print(5)
                    else:
                        print(0)
                else:
                    x0 = f/c
                    print(3, x0)
            else:
                if c == 0:
                    y0 = f/d
                    print(4,y0)
                else:
                    k = -c/d
                    _b = f/d
                    print(1, k, _b)
        else:
            print(0)
        
    else:
        if c == 0:
            if d == 0:
                if f == 0:
                    y0 = e/b
                    print(4,y0)
                else:
                    print(0)
            else:
                if abs(e/b - f/d) > 0.00001:
                    print(0)
                else:
                    y0 = e/b
                    print(4, y0)
        else:
            x = (f-d*e/b)/c
            y = e/b
            print(2, x, y)
else:
    if b == 0:
        if d == 0:
            if c== 0:
                if f == 0:
                    x0 = e/a
                    print(3, x0)
                else:
                    print(0)
            else:
                if abs(e/a - f/c) > 0.00001:
                    print(0)
                else:
                    x0 = e/a
                    print(3, x0)
            
        else:
            x = e/a
            y = f/d - c*e/(a*d)
            print(2, x, y)
    else:
        if c == 0:
            if d == 0:
                if f == 0:
                    k = -a/b
                    _b = e/b
                    print(1, k, _b)
                else:
                    print(0)
            else:
                y = f/d
                x = (e-b*y)/a
                print(2, x, y)
        else:
            if d == 0:
                x = f/c
                y = (e-a*f/c)/b
                print(2, x, y)
            else:
                if f*a-e*c == 0:
                    if d*a-b*c == 0:
                        k = -a/b
                        _b = e/b
                        print(1, k, _b)
                    else:
                        print(0)
                else:
                    if d*a-b*c == 0:
                        print(0)
                    else:
                        y = (f*a-e*c)/(d*a-b*c)
                        x = (e-b*y)/a
                        print(2, x, y)

