
x=100  # Red value
x2= 50
y=0  # Green value
y2=100
z=0  # Blue value
z2=0
w=0  # Readiness value
w2=200

# Get pixel brightnesses
result=(x+y+z)/3
result2 = (x2+y2+z2)/3

# Get mean brightness
result3 = (result + result2) / 2
print(result3)